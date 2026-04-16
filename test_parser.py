"""Test file parsing module - Enhanced version"""
import re
import logging
from typing import List, Dict, Tuple

logger = logging.getLogger(__name__)

class TestParser:
    """Parses test files to extract questions and answers"""
    
    @staticmethod
    def clean_text(text: str) -> str:
        """Clean text from PDF/DOCX artifacts"""
        # Normalize line breaks
        text = text.replace('\r\n', '\n')
        text = text.replace('\r', '\n')
        # Remove extra spaces around lines but keep structure
        lines = text.split('\n')
        lines = [line.strip() for line in lines]
        text = '\n'.join(lines)
        return text.strip()
    
    @staticmethod
    def parse_numbered_format(content: str) -> List[Dict]:
        """
        Parse numbered format:
        1) Question?
        a) Answer 1
        b) Answer 2 (correct)
        c) Answer 3
        """
        questions = []
        lines = content.split('\n')
        
        logger.info(f"parse_numbered_format: Processing {len(lines)} lines")
        logger.info(f"First 10 non-empty lines:")
        count = 0
        for i, line in enumerate(lines[:100]):
            if line.strip():
                logger.info(f"  Line {i}: '{line[:80]}'")
                count += 1
                if count >= 10:
                    break
        
        current_question = None
        current_q_num = None
        current_options = []
        correct_answer_index = -1
        
        for line in lines:
            line = line.strip()
            if not line:
                continue
            
            # Check for question: 1) 2) 3) etc
            q_match = re.match(r'^(\d+)[.)]\s*(.+)$', line)
            if q_match:
                logger.info(f"  Q Match: {line}")
                # Save previous question
                if current_question and len(current_options) >= 2:
                    questions.append({
                        'question': current_question,
                        'options': current_options,
                        'correct_option_id': correct_answer_index if correct_answer_index >= 0 else 0
                    })
                
                current_q_num = q_match.group(1)
                current_question = q_match.group(2)
                current_options = []
                correct_answer_index = -1
                continue
            
            # Check for answer: a) b) c) etc
            a_match = re.match(r'^[a-z][.)]\s*(.+)$', line)
            if a_match and current_question:
                logger.info(f"  A Match: {line}")
                answer_text = a_match.group(1)
                
                # Check if marked as correct
                is_correct = '(correct)' in answer_text.lower() or '(to\'g\'ri)' in answer_text.lower()
                if is_correct:
                    answer_text = re.sub(r'\s*\(correct\)|\s*\(to\'g\'ri\)', '', answer_text, flags=re.IGNORECASE).strip()
                    correct_answer_index = len(current_options)
                
                if answer_text:
                    current_options.append(answer_text)
        
        # Add last question
        if current_question and len(current_options) >= 2:
            questions.append({
                'question': current_question,
                'options': current_options,
                'correct_option_id': correct_answer_index if correct_answer_index >= 0 else 0
            })
        
        logger.info(f"parse_numbered_format: Found {len(questions)} questions")
        return questions
    
    @staticmethod
    def parse_qa_format(content: str) -> List[Dict]:
        """
        Parse Q/A format:
        Q: Question?
        A: Answer 1
        A: Answer 2
        A: Correct Answer*
        """
        questions = []
        lines = content.split('\n')
        
        current_question = None
        current_options = []
        correct_answer_index = -1
        
        for line in lines:
            line = line.strip()
            if not line:
                continue
            
            # Question line
            if line.upper().startswith('Q:') or line.upper().startswith('Q.'):
                # Save previous question
                if current_question and len(current_options) >= 2:
                    questions.append({
                        'question': current_question,
                        'options': current_options,
                        'correct_option_id': correct_answer_index if correct_answer_index >= 0 else 0
                    })
                
                current_question = re.sub(r'^[Qq][:\.]\s*', '', line)
                current_options = []
                correct_answer_index = -1
                continue
            
            # Answer line
            if line.upper().startswith('A:') or line.upper().startswith('A.'):
                if current_question:
                    answer_text = re.sub(r'^[Aa][:\.]\s*', '', line)
                    
                    # Check for correct marker
                    if answer_text.endswith('*'):
                        answer_text = answer_text[:-1].strip()
                        correct_answer_index = len(current_options)
                    
                    if answer_text:
                        current_options.append(answer_text)
        
        # Add last question
        if current_question and len(current_options) >= 2:
            questions.append({
                'question': current_question,
                'options': current_options,
                'correct_option_id': correct_answer_index if correct_answer_index >= 0 else 0
            })
        
        logger.info(f"parse_qa_format: Found {len(questions)} questions")
        return questions
    
    @staticmethod
    def parse_simple_numbered_format(content: str) -> List[Dict]:
        """
        Parse simple numbered format (no parenthesis/dots):
        1 Question text?
        a answer 1
        b answer 2
        c answer 3
        
        2 Another question?
        a answer 1
        b answer 2
        """
        questions = []
        lines = content.split('\n')
        
        current_question = None
        current_q_num = None
        current_options = []
        correct_answer_index = -1
        
        for line in lines:
            line = line.strip()
            if not line:
                continue
            
            # Check for question: "1 " "2 " etc (number followed by space)
            q_match = re.match(r'^(\d+)\s+(.+)$', line)
            if q_match and line.endswith('?'):
                logger.info(f"  Simple Num Q Match: {line}")
                # Save previous question
                if current_question and len(current_options) >= 2:
                    questions.append({
                        'question': current_question,
                        'options': current_options,
                        'correct_option_id': correct_answer_index if correct_answer_index >= 0 else 0
                    })
                
                current_q_num = q_match.group(1)
                current_question = q_match.group(2)
                current_options = []
                correct_answer_index = -1
                continue
            
            # Check for answer: "a " "b " "c " etc (letter followed by space)
            a_match = re.match(r'^[a-z]\s+(.+)$', line)
            if a_match and current_question:
                logger.info(f"  Simple Num A Match: {line}")
                answer_text = a_match.group(1)
                
                # Check if marked as correct
                is_correct = answer_text.endswith('*') or '(to\'g\'ri)' in answer_text.lower() or '(correct)' in answer_text.lower()
                if is_correct:
                    answer_text = re.sub(r'\*$|\s*\(correct\)|\s*\(to\'g\'ri\)', '', answer_text, flags=re.IGNORECASE).strip()
                    correct_answer_index = len(current_options)
                
                if answer_text:
                    current_options.append(answer_text)
        
        # Add last question
        if current_question and len(current_options) >= 2:
            questions.append({
                'question': current_question,
                'options': current_options,
                'correct_option_id': correct_answer_index if correct_answer_index >= 0 else 0
            })
        
        logger.info(f"parse_simple_numbered_format: Found {len(questions)} questions")
        return questions
    
    @staticmethod
    def parse_unnumbered_format(content: str) -> List[Dict]:
        """
        Parse unnumbered format (no numbers on questions/answers):
        Question text?
        Answer 1
        Answer 2
        Answer 3
        
        Another question text?
        Answer 1
        Answer 2
        """
        questions = []
        lines = content.split('\n')
        
        current_question = None
        current_options = []
        
        for line in lines:
            line = line.strip()
            if not line or line.startswith('-') or line.startswith('•'):
                # Skip empty lines and bullet points
                continue
            
            # Check if line is a question (ends with ? or looks like one)
            is_question = line.endswith('?')
            
            if is_question:
                # Save previous question if we have one
                if current_question and len(current_options) >= 2:
                    questions.append({
                        'question': current_question,
                        'options': current_options,
                        'correct_option_id': 0  # Default to first option
                    })
                
                current_question = line
                current_options = []
            elif current_question:
                # This is an answer to current question
                # Skip lines that look like metadata or formatting
                if len(line) > 2 and not line.startswith('www') and not '@' in line:
                    current_options.append(line)
        
        # Add last question
        if current_question and len(current_options) >= 2:
            questions.append({
                'question': current_question,
                'options': current_options,
                'correct_option_id': 0
            })
        
        logger.info(f"parse_unnumbered_format: Found {len(questions)} questions")
        return questions
    
    @staticmethod
    def detect_format(content: str) -> str:
        """Detect test format"""
        # Count Q: and A: patterns
        q_count = len(re.findall(r'^[Qq][:\.]\s*', content, re.MULTILINE))
        a_count = len(re.findall(r'^[Aa][:\.]\s*', content, re.MULTILINE))
        
        # Count numbered patterns (1) 2) etc)
        num_count = len(re.findall(r'^\d+[.)]\s*', content, re.MULTILINE))
        letter_count = len(re.findall(r'^[a-z][.)]\s*', content, re.MULTILINE))
        
        # Count simple numbered patterns (1 2 3 with space, followed by question mark)
        simple_num_q_count = len(re.findall(r'^\d+\s+.*\?$', content, re.MULTILINE))
        simple_num_a_count = len(re.findall(r'^[a-z]\s+', content, re.MULTILINE))
        
        # Count question marks
        q_mark_count = content.count('?')
        
        # Decide format
        if q_count > 0:
            return "Q/A"
        elif simple_num_q_count >= 2 and simple_num_a_count >= 4:
            return "SimpleNumbered"
        elif num_count >= 5:
            return "Numbered"
        elif q_mark_count >= 5:
            return "Unnumbered"
        else:
            return "Unnumbered"  # Default to unnumbered since most files seem to be
    
    @staticmethod
    def parse(content: str) -> Tuple[List[Dict], str]:
        """
        Parse test content - auto-detect format
        Returns: (questions_list, format_name)
        """
        if not content or len(content.strip()) < 10:
            return [], "Empty"
        
        # Clean content
        content = TestParser.clean_text(content)
        logger.info(f"parse: Content cleaned, length={len(content)}")
        
        # Detect format
        fmt = TestParser.detect_format(content)
        logger.info(f"parse: Detected format: {fmt}")
        
        # Parse based on format
        if fmt == "Q/A":
            questions = TestParser.parse_qa_format(content)
            if questions:
                return questions, "Q/A format"
        elif fmt == "SimpleNumbered":
            questions = TestParser.parse_simple_numbered_format(content)
            if questions:
                return questions, "Simple Numbered format"
        elif fmt == "Numbered":
            questions = TestParser.parse_numbered_format(content)
            if questions:
                return questions, "Numbered format"
        elif fmt == "Unnumbered":
            questions = TestParser.parse_unnumbered_format(content)
            if questions:
                return questions, "Unnumbered format"
        
        # Try all formats as fallback
        questions = TestParser.parse_simple_numbered_format(content)
        if questions:
            return questions, "Simple Numbered format"
        
        questions = TestParser.parse_unnumbered_format(content)
        if questions:
            return questions, "Unnumbered format"
        
        questions = TestParser.parse_numbered_format(content)
        if questions:
            return questions, "Numbered format"
        
        questions = TestParser.parse_qa_format(content)
        if questions:
            return questions, "Q/A format"
        
        return [], "Invalid format"
