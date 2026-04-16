"""Quiz storage and management module"""
import json
import os
from typing import List, Dict, Optional
from datetime import datetime

class QuizStorage:
    """Manages quiz storage and retrieval"""
    
    def __init__(self, storage_dir: str = "quizzes"):
        self.storage_dir = storage_dir
        if not os.path.exists(storage_dir):
            os.makedirs(storage_dir)
    
    def save_quiz(self, quiz_name: str, questions: List[Dict], user_id: int) -> str:
        """Save quiz and return quiz ID"""
        quiz_id = f"{user_id}_{datetime.now().strftime('%Y%m%d_%H%M%S')}_{quiz_name[:20]}"
        
        quiz_data = {
            'id': quiz_id,
            'name': quiz_name,
            'user_id': user_id,
            'created_at': datetime.now().isoformat(),
            'updated_at': datetime.now().isoformat(),
            'questions': questions
        }
        
        file_path = os.path.join(self.storage_dir, f"{quiz_id}.json")
        with open(file_path, 'w', encoding='utf-8') as f:
            json.dump(quiz_data, f, ensure_ascii=False, indent=2)
        
        return quiz_id
    
    def get_quiz(self, quiz_id: str) -> Optional[Dict]:
        """Retrieve quiz by ID"""
        file_path = os.path.join(self.storage_dir, f"{quiz_id}.json")
        
        if not os.path.exists(file_path):
            return None
        
        with open(file_path, 'r', encoding='utf-8') as f:
            return json.load(f)
    
    def get_user_quizzes(self, user_id: int) -> List[Dict]:
        """Get all quizzes for a user"""
        quizzes = []
        
        for filename in os.listdir(self.storage_dir):
            if filename.startswith(f"{user_id}_") and filename.endswith('.json'):
                file_path = os.path.join(self.storage_dir, filename)
                with open(file_path, 'r', encoding='utf-8') as f:
                    quizzes.append(json.load(f))
        
        return sorted(quizzes, key=lambda x: x['created_at'], reverse=True)
    
    def update_quiz(self, quiz_id: str, questions: List[Dict]) -> bool:
        """Update quiz questions"""
        quiz = self.get_quiz(quiz_id)
        if not quiz:
            return False
        
        quiz['questions'] = questions
        quiz['updated_at'] = datetime.now().isoformat()
        
        file_path = os.path.join(self.storage_dir, f"{quiz_id}.json")
        with open(file_path, 'w', encoding='utf-8') as f:
            json.dump(quiz, f, ensure_ascii=False, indent=2)
        
        return True
    
    def delete_quiz(self, quiz_id: str) -> bool:
        """Delete a quiz"""
        file_path = os.path.join(self.storage_dir, f"{quiz_id}.json")
        
        if not os.path.exists(file_path):
            return False
        
        os.remove(file_path)
        return True
    
    def update_question(self, quiz_id: str, question_index: int, 
                       new_question: str = None, new_options: List[str] = None,
                       new_correct_option: int = None) -> bool:
        """Update a specific question in a quiz"""
        quiz = self.get_quiz(quiz_id)
        if not quiz or question_index >= len(quiz['questions']):
            return False
        
        question = quiz['questions'][question_index]
        
        if new_question:
            question['question'] = new_question
        if new_options:
            question['options'] = new_options
        if new_correct_option is not None:
            question['correct_option_id'] = new_correct_option
        
        quiz['updated_at'] = datetime.now().isoformat()
        
        file_path = os.path.join(self.storage_dir, f"{quiz_id}.json")
        with open(file_path, 'w', encoding='utf-8') as f:
            json.dump(quiz, f, ensure_ascii=False, indent=2)
        
        return True
