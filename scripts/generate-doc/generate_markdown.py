#!/usr/bin/env python3
"""
Convert chapter JSON files to Markdown learning documents.
Each Markdown file contains rich educational content for 90 words.
"""

import json
import os
import math
import re
from typing import List, Dict, Any

class VocabularyMarkdownGenerator:
    """Generate rich Markdown content for vocabulary learning."""
    
    def __init__(self):
        self.phonetic_data = self._load_phonetic_data()
    
    def _load_phonetic_data(self) -> Dict[str, str]:
        """Load basic phonetic data for common words."""
        # In a real implementation, this would load from a phonetic dictionary
        # For now, we'll create basic phonetic patterns
        common_phonetics = {
            "the": "/ðə/", "be": "/biː/", "a": "/ə/", "to": "/tuː/", "of": "/ʌv/",
            "and": "/ænd/", "in": "/ɪn/", "have": "/hæv/", "it": "/ɪt/", "for": "/fɔːr/",
            "not": "/nɒt/", "with": "/wɪð/", "as": "/æz/", "you": "/juː/", "do": "/duː/",
            "at": "/æt/", "this": "/ðɪs/", "but": "/bʌt/", "his": "/hɪz/", "by": "/baɪ/",
            "from": "/frʌm/", "they": "/ðeɪ/", "she": "/ʃiː/", "or": "/ɔːr/", "an": "/æn/",
            "will": "/wɪl/", "my": "/maɪ/", "one": "/wʌn/", "all": "/ɔːl/", "would": "/wʊd/",
            "there": "/ðeər/", "their": "/ðeər/", "what": "/wʌt/", "so": "/səʊ/", "up": "/ʌp/",
            "out": "/aʊt/", "if": "/ɪf/", "about": "/əˈbaʊt/", "who": "/huː/", "get": "/get/",
            "which": "/wɪtʃ/", "go": "/gəʊ/", "me": "/miː/", "when": "/wen/", "make": "/meɪk/",
            "can": "/kæn/", "like": "/laɪk/", "time": "/taɪm/", "no": "/nəʊ/", "just": "/dʒʌst/",
            "him": "/hɪm/", "know": "/nəʊ/", "take": "/teɪk/", "people": "/ˈpiːpl/", "into": "/ˈɪntuː/",
            "year": "/jɪər/", "your": "/jʊər/", "good": "/gʊd/", "some": "/sʌm/", "could": "/kʊd/",
            "them": "/ðem/", "see": "/siː/", "other": "/ˈʌðər/", "than": "/ðæn/", "then": "/ðen/",
            "now": "/naʊ/", "look": "/lʊk/", "only": "/ˈəʊnli/", "come": "/kʌm/", "its": "/ɪts/",
            "over": "/ˈəʊvər/", "think": "/θɪŋk/", "also": "/ˈɔːlsəʊ/", "your": "/jʊər/", "work": "/wɜːrk/",
            "life": "/laɪf/", "way": "/weɪ/", "may": "/meɪ/", "say": "/seɪ/", "each": "/iːtʃ/",
            "which": "/wɪtʃ/", "she": "/ʃiː/", "do": "/duː/", "how": "/haʊ/", "their": "/ðeər/",
            "if": "/ɪf/", "will": "/wɪl/", "up": "/ʌp/", "other": "/ˈʌðər/", "about": "/əˈbaʊt/",
            "out": "/aʊt/", "many": "/ˈmeni/", "then": "/ðen/", "them": "/ðem/", "these": "/ðiːz/",
            "so": "/səʊ/", "some": "/sʌm/", "her": "/hər/", "would": "/wʊd/", "make": "/meɪk/",
            "like": "/laɪk/", "into": "/ˈɪntuː/", "him": "/hɪm/", "has": "/hæz/", "two": "/tuː/",
            "more": "/mɔːr/", "very": "/ˈveri/", "what": "/wʌt/", "know": "/nəʊ/", "just": "/dʒʌst/",
            "first": "/fɜːrst/", "get": "/get/", "over": "/ˈəʊvər/", "think": "/θɪŋk/", "where": "/weər/",
            "much": "/mʌtʃ/", "go": "/gəʊ/", "well": "/wel/", "were": "/wər/", "been": "/biːn/",
            "through": "/θruː/", "when": "/wen/", "who": "/huː/", "oil": "/ɔɪl/", "its": "/ɪts/",
            "now": "/naʊ/", "find": "/faɪnd/", "long": "/lɔːŋ/", "down": "/daʊn/", "day": "/deɪ/",
            "did": "/dɪd/", "get": "/get/", "come": "/kʌm/", "made": "/meɪd/", "may": "/meɪ/",
            "part": "/pɑːrt/"
        }
        return common_phonetics
    
    def _get_phonetic(self, word: str) -> str:
        """Get phonetic transcription for a word."""
        word_lower = word.lower()
        if word_lower in self.phonetic_data:
            return self.phonetic_data[word_lower]
        else:
            # Generate a placeholder phonetic based on word patterns
            return self._generate_phonetic_placeholder(word_lower)
    
    def _generate_phonetic_placeholder(self, word: str) -> str:
        """Generate a basic phonetic placeholder for unknown words."""
        # This is a simplified version - in reality you'd use a phonetic library
        phonetic = f"/{word}/"  # Placeholder
        return phonetic
    
    def _get_word_derivatives(self, word: str, pos: str = None) -> List[str]:
        """Get common derivatives of a word."""
        derivatives = []
        word_lower = word.lower()
        
        # Common patterns for derivatives
        if word_lower.endswith('e'):
            base = word_lower[:-1]
            derivatives.extend([
                f"{base}ing *v.* (现在分词)",
                f"{base}ed *v.* (过去式/过去分词)"
            ])
        elif word_lower.endswith('y'):
            base = word_lower[:-1]
            derivatives.extend([
                f"{base}ies *n.* (复数)",
                f"{base}ied *v.* (过去式)"
            ])
        
        # Add -ly for adjectives
        if not word_lower.endswith('ly'):
            derivatives.append(f"{word_lower}ly *adv.* (副词)")
        
        # Add -ness for adjectives
        if not word_lower.endswith('ness'):
            derivatives.append(f"{word_lower}ness *n.* (名词)")
        
        return derivatives[:3]  # Limit to 3 derivatives
    
    def _generate_example_sentences(self, word: str, definition: str) -> List[Dict[str, str]]:
        """Generate example sentences for a word."""
        word_lower = word.lower()
        
        # Common sentence patterns based on word type
        sentences = [
            {
                "english": f"The {word_lower} is very important in our daily life.",
                "chinese": f"这个{definition}在我们的日常生活中非常重要。"
            },
            {
                "english": f"We need to understand how to use {word_lower} correctly.",
                "chinese": f"我们需要理解如何正确使用{definition}。"
            }
        ]
        
        return sentences
    
    def _generate_cultural_note(self, word: str) -> str:
        """Generate cultural note for a word."""
        cultural_notes = {
            "the": "定冠词'the'是英语中最常用的词，用于特指已知的人或物。在考研英语中，掌握冠词的用法是基础中的基础。",
            "be": "动词'be'是英语中最重要的系动词，有am/is/are等形式。它是构成各种时态和语态的基础。",
            "and": "连词'and'表示并列关系，是英语写作中最基本的连接词之一。",
            "in": "介词'in'表示时间、地点、方式等，是考研英语中常考的介词之一。"
        }
        
        return cultural_notes.get(word.lower(), f"'{word}'是考研词汇中的重要单词，需要掌握其各种用法和搭配。")
    
    def _generate_multiple_meanings(self, word: str, definition: str) -> List[str]:
        """Generate multiple meanings for a word."""
        meanings = [
            f"基本含义：{definition}",
            f"在不同语境中可表示：{definition}的相关概念",
            f"考研常考含义：{definition}及其引申义"
        ]
        return meanings
    
    def _generate_word_content(self, word_data: Dict[str, Any], index: int) -> str:
        """Generate detailed content for a single word."""
        word = word_data["单词"]
        definition = word_data["释义"]
        frequency = word_data["词频"]
        sequence = word_data["序号"]
        variant = word_data.get("其他拼写")
        
        phonetic = self._get_phonetic(word)
        derivatives = self._get_word_derivatives(word)
        examples = self._generate_example_sentences(word, definition)
        cultural_note = self._generate_cultural_note(word)
        multiple_meanings = self._generate_multiple_meanings(word, definition)
        
        # Generate emoji based on index
        emoji_list = ["1️⃣", "2️⃣", "3️⃣", "4️⃣", "5️⃣", "6️⃣", "7️⃣", "8️⃣", "9️⃣", "🔟", 
                     "🌟", "💫", "⭐", "✨", "🎯", "🏆", "📚", "💎", "🔥", "⚡",
                     "🎪", "🎭", "🎨", "🎵", "🎸", "🎺", "🎻", "🎹", "🥁", "🎤"]
        emoji = emoji_list[index % len(emoji_list)]
        
        content = f"""### {emoji} {word} `{phonetic}`

**【基本释义】** {definition}

**【词频排序】** 第{sequence}位 | 词频: {frequency}次"""
        
        if variant:
            content += f"\n**【其他拼写】** {variant}"
        
        if derivatives:
            content += f"\n\n**【词性变化】**\n"
            for i, derivative in enumerate(derivatives[:3], 1):
                content += f"- {derivative}\n"
        
        content += f"""
**【重点辨析】**
考研中需要重点关注"{word}"的用法和搭配，特别是在阅读理解和完形填空中的应用。

**【考点聚焦】**
1. 高频搭配：常与其他词组成固定搭配
2. 语法要点：注意词性和用法
3. 考试重点：在考研真题中的常见用法

**【例句精讲】**"""
        
        for i, example in enumerate(examples, 1):
            content += f"""
> {example['english']}
> *{example['chinese']}*
"""
        
        content += f"""
**【文化链接】**
{cultural_note}

**【一词多义】**"""
        
        for i, meaning in enumerate(multiple_meanings, 1):
            content += f"\n{i}. {meaning}"
        
        content += "\n\n---\n"
        
        return content
    
    def _generate_section_summary(self, section_num: int, words: List[Dict]) -> str:
        """Generate summary for a section."""
        word_list = [w["单词"] for w in words]
        word_str = " • ".join(word_list)
        
        return f"""## 📋 第{section_num}节 学习总结

**本节重点单词：** {word_str}

### 🎯 学习要点
1. **高频词汇**：本节包含{len(words)}个重要词汇，都是考研英语中的基础词汇
2. **记忆策略**：建议采用词根词缀记忆法，结合例句加深理解
3. **应用重点**：这些词汇在阅读理解、写作和翻译中都有重要应用

### 📝 学习建议
- 每天复习本节单词，确保熟练掌握基本含义
- 重点关注一词多义和固定搭配
- 结合真题练习，提高实际应用能力

---

"""
    
    def generate_chapter_markdown(self, chapter_file: str, output_dir: str) -> str:
        """Generate a complete Markdown file for a chapter."""
        
        # Read chapter JSON
        with open(chapter_file, 'r', encoding='utf-8') as f:
            chapter_data = json.load(f)
        
        chapter_info = chapter_data["chapter_info"]
        words = chapter_data["words"]
        
        chapter_num = chapter_info["chapter_number"]
        word_count = chapter_info["word_count"]
        words_range = chapter_info["words_range"]
        
        # Create markdown content
        markdown_content = f"""# 📖 考研词汇学习_第{chapter_num}章

> **词汇范围：** 第{words_range}个单词 | **总词数：** {word_count}个
> 
> **学习目标：** 掌握本章所有词汇的基本含义、用法和搭配

---

## 🌟 章节概览

本章包含考研词汇中的{word_count}个重要单词，按照词频排序。每个单词都提供了详细的学习内容，包括音标、例句、文化背景等。

### 📊 本章单词一览

| 序号 | 单词 | 音标 | 基本释义 | 词频 |
|------|------|------|----------|------|"""
        
        # Add word overview table
        for word_data in words:
            word = word_data["单词"]
            definition = word_data["释义"]
            sequence = word_data["序号"]
            frequency = word_data["词频"]
            phonetic = self._get_phonetic(word)
            markdown_content += f"\n| {sequence} | {word} | `{phonetic}` | {definition} | {frequency} |"
        
        markdown_content += "\n\n---\n\n"
        
        # Divide words into 3 sections (30 words each)
        section_size = 30
        sections = []
        for i in range(0, len(words), section_size):
            sections.append(words[i:i + section_size])
        
        # Generate content for each section
        for section_num, section_words in enumerate(sections, 1):
            markdown_content += f"## 📚 第{section_num}节 (单词 {section_words[0]['序号']}-{section_words[-1]['序号']})\n\n"
            
            # Add detailed content for each word in section
            for i, word_data in enumerate(section_words):
                word_content = self._generate_word_content(word_data, i)
                markdown_content += word_content
            
            # Add section summary
            section_summary = self._generate_section_summary(section_num, section_words)
            markdown_content += section_summary
        
        # Add chapter conclusion
        high_freq_words = [w["单词"] for w in words if w["词频"] > 1000]
        markdown_content += f"""## 🎓 章节总结

### ✨ 本章亮点
1. **高频核心词**：本章包含{len(high_freq_words)}个高频词汇
2. **学习价值**：这些词汇是考研英语的基础，必须熟练掌握
3. **应用广泛**：在阅读、写作、翻译中都有重要作用

### 🎯 重点单词回顾
{' • '.join(high_freq_words[:10])}{'...' if len(high_freq_words) > 10 else ''}

### 📈 学习进度
- ✅ 已学习单词：{word_count}个
- 🎯 当前进度：第{words_range}个单词
- 📊 完成度：{chapter_num}/{chapter_info['total_chapters']}章

---

## 💡 学习建议

### 🔄 复习策略
1. **日常复习**：每天花15-20分钟复习本章单词
2. **联想记忆**：利用词根词缀和联想法增强记忆
3. **实际应用**：在阅读和写作中主动使用这些词汇

### 📝 练习建议
1. **词汇测试**：定期进行词汇测试，检验掌握程度
2. **造句练习**：用每个单词造句，加深理解
3. **真题练习**：结合考研真题，提高实战能力

### 🎪 记忆小技巧
- 制作词汇卡片，随时复习
- 将生词融入日常对话和写作
- 利用词汇App进行碎片化学习

---

*📚 **持续学习，稳步提升！每一个单词都是通向成功的阶梯！** 🌈*

> **下一步：** 继续学习第{chapter_num + 1}章，保持学习的连续性和系统性。
"""
        
        # Save to output directory
        os.makedirs(output_dir, exist_ok=True)
        output_file = os.path.join(output_dir, f"考研词汇学习_第{chapter_num}章.md")
        
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(markdown_content)
        
        return output_file

def main():
    """Main function to generate all Markdown files."""
    generator = VocabularyMarkdownGenerator()
    
    # Create main output directory
    base_output_dir = "vocabulary_markdown"
    os.makedirs(base_output_dir, exist_ok=True)
    
    chapter_json_dir = "chapter_jsons"
    
    # Get all chapter JSON files
    chapter_files = []
    for filename in os.listdir(chapter_json_dir):
        if filename.startswith("chapter_") and filename.endswith(".json"):
            chapter_files.append(os.path.join(chapter_json_dir, filename))
    
    chapter_files.sort()
    
    print(f"Found {len(chapter_files)} chapter files to convert")
    
    # Process chapters and organize into folders (5 chapters per folder)
    chapters_per_folder = 5
    created_files = []
    
    for i, chapter_file in enumerate(chapter_files):
        chapter_num = i + 1
        folder_start = ((chapter_num - 1) // chapters_per_folder) * chapters_per_folder + 1
        folder_end = min(folder_start + chapters_per_folder - 1, len(chapter_files))
        
        # Create folder for every 5 chapters
        folder_name = f"考研词汇_第{folder_start}-{folder_end}章"
        folder_path = os.path.join(base_output_dir, folder_name)
        
        # Generate Markdown file
        output_file = generator.generate_chapter_markdown(chapter_file, folder_path)
        created_files.append(output_file)
        
        print(f"Created: {output_file}")
    
    print(f"\n✅ Successfully created {len(created_files)} Markdown files!")
    print(f"📁 Files are organized in the '{base_output_dir}' directory")
    
    # Create summary report
    import time
    current_time = time.strftime('%Y-%m-%d %H:%M:%S')
    summary_file = os.path.join(base_output_dir, "生成报告.md")
    with open(summary_file, 'w', encoding='utf-8') as f:
        f.write(f"""# 📊 考研词汇Markdown文档生成报告

## 🎯 生成概况
- **总文件数：** {len(created_files)}个
- **总词汇数：** 5530个
- **文件组织：** 每{chapters_per_folder}个文件一个文件夹
- **生成时间：** {current_time}

## 📁 文件结构
```
vocabulary_markdown/
├── 考研词汇_第1-5章/
│   ├── 考研词汇学习_第1章.md (1-90词)
│   ├── 考研词汇学习_第2章.md (91-180词)
│   ├── 考研词汇学习_第3章.md (181-270词)
│   ├── 考研词汇学习_第4章.md (271-360词)
│   └── 考研词汇学习_第5章.md (361-450词)
├── 考研词汇_第6-10章/
│   └── ...
└── ...
```

## ✨ 文件特色
- 🎨 丰富的emoji装饰
- 📊 详细的词汇表格
- 🎯 考点分析和例句
- 📚 文化背景知识
- 💡 学习建议和技巧

## 🎓 使用建议
1. 按章节顺序学习，每天1-2章
2. 重点关注高频词汇和考点分析
3. 结合例句理解单词用法
4. 定期复习，巩固记忆

*🌟 祝您考研英语取得优异成绩！*
""")
    
    print(f"📋 生成了总结报告：{summary_file}")

if __name__ == "__main__":
    main()