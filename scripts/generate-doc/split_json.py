#!/usr/bin/env python3
"""
Split the main netem_full_list.json into smaller JSON files for each chapter.
Each chapter contains 90 words (3 sections of 30 words each).
"""

import json
import os
import math

def split_json_into_chapters():
    """Split the main JSON file into chapter-based JSON files."""
    
    # Read the main JSON file
    input_file = "../../netem_full_list.json"
    
    with open(input_file, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    words = data["5530考研词汇词频排序表"]
    print(f"Total words to process: {len(words)}")
    
    # Calculate number of chapters (90 words per chapter)
    words_per_chapter = 90
    total_chapters = math.ceil(len(words) / words_per_chapter)
    
    print(f"Will create {total_chapters} chapters with {words_per_chapter} words each")
    
    # Create output directory for chapter JSON files
    output_dir = "chapter_jsons"
    os.makedirs(output_dir, exist_ok=True)
    
    # Split words into chapters
    for chapter_num in range(1, total_chapters + 1):
        start_idx = (chapter_num - 1) * words_per_chapter
        end_idx = min(start_idx + words_per_chapter, len(words))
        
        chapter_words = words[start_idx:end_idx]
        
        # Create chapter data structure
        chapter_data = {
            "chapter_info": {
                "chapter_number": chapter_num,
                "total_chapters": total_chapters,
                "words_range": f"{start_idx + 1}-{end_idx}",
                "word_count": len(chapter_words)
            },
            "words": chapter_words
        }
        
        # Save to file
        output_file = os.path.join(output_dir, f"chapter_{chapter_num:02d}.json")
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(chapter_data, f, ensure_ascii=False, indent=2)
        
        print(f"Created {output_file} with {len(chapter_words)} words (序号 {start_idx + 1}-{end_idx})")
    
    print(f"\nSuccessfully created {total_chapters} chapter JSON files in '{output_dir}' directory")
    
    return total_chapters

if __name__ == "__main__":
    split_json_into_chapters()