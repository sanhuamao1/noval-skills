#!/usr/bin/env python3
# .claude/hooks/insertToOutline.py

import json
import sys
import re
from pathlib import Path

def log(msg):
    """输出到 stderr，这样手动运行也能看到，且不干扰 JSON 输出"""
    print(f"[insertToOutline] {msg}", file=sys.stderr)

def read_hook_input():
    """安全读取 stdin，不支持交互式手动运行"""
    if sys.stdin.isatty():
        # 手动运行时，没有 JSON 输入，直接返回 True 表示执行
        log("手动运行模式，跳过 stdin 解析")
        return True
    try:
        data = json.load(sys.stdin)
        tool_input = data.get("tool_input", {})
        file_path = tool_input.get("file_path", "")
        log(f"触发文件: {file_path}")
        return "temp/output.md" in file_path
    except Exception as e:
        log(f"读取 stdin 失败: {e}，默认执行")
        return True

def parse_sections(content):
    """按 --- 分割，返回 (long_part, short_part)"""
    parts = content.split("---", 1)
    long_part = parts[0].strip()
    short_part = parts[1].strip() if len(parts) > 1 else ""
    log(f"分割结果：长纲长度 {len(long_part)}，短纲长度 {len(short_part)}")
    return long_part, short_part

def extract_chapter_number(text):
    """从文本开头提取章节号，如 '第3章' -> 3"""
    match = re.search(r'^####\s*第(\d+)章', text, re.MULTILINE)
    if match:
        return int(match.group(1))
    return None

def append_to_file(file_path, new_content, chapter_num):
    """将 new_content 追加到对应章节后面"""
    file_path = Path(file_path)
    log(f"处理文件: {file_path}，章节号: {chapter_num}")

    if not file_path.exists():
        log("目标文件不存在，直接写入")
        file_path.write_text(new_content + "\n", encoding="utf-8")
        return

    original = file_path.read_text(encoding="utf-8")
    lines = original.splitlines(keepends=True)

    # 查找章节标题行
    chapter_pattern = re.compile(rf'^####\s*第{chapter_num}章\s.*$')
    chapter_start_idx = None
    for i, line in enumerate(lines):
        if chapter_pattern.match(line.strip()):
            chapter_start_idx = i
            break

    if chapter_start_idx is None:
        log("未找到对应章节，追加到文件末尾")
        with open(file_path, "a", encoding="utf-8") as f:
            f.write("\n" + new_content + "\n")
        return

    # 找到章节结束位置：下一个章节标题或文件末尾
    next_chapter_pattern = re.compile(r'^####\s*第\d+章\s.*$')
    chapter_end_idx = len(lines)
    for i in range(chapter_start_idx + 1, len(lines)):
        if next_chapter_pattern.match(lines[i].strip()):
            chapter_end_idx = i
            break

    log(f"找到章节起始行 {chapter_start_idx}，结束行 {chapter_end_idx}，插入新内容")
    lines[chapter_end_idx:chapter_end_idx] = [new_content + "\n"]
    file_path.write_text("".join(lines), encoding="utf-8")

def main():
    # 定位项目根目录：脚本位于 .claude/hooks/ 下，向上两级才是项目根
    script_path = Path(__file__).resolve()
    project_root = script_path.parent.parent.parent
    log(f"项目根目录: {project_root}")

    temp_md = project_root / "temp" / "output.md"
    outline_long = project_root / "standards" / "story-outline.md"
    outline_short = project_root / "standards" / "story-outline-short.md"

    log(f"temp 文件: {temp_md}")
    log(f"长纲文件: {outline_long}")
    log(f"短纲文件: {outline_short}")

    if not read_hook_input():
        log("未匹配到 temp/output.md，退出")
        return

    if not temp_md.exists():
        log(f"temp 文件不存在: {temp_md}，退出")
        return

    content = temp_md.read_text(encoding="utf-8")
    log(f"读取到内容长度: {len(content)}")

    long_part, short_part = parse_sections(content)

    # 提取章节号
    chapter_num = extract_chapter_number(long_part)
    if chapter_num is None:
        log("无法提取章节号，将直接追加")
    else:
        log(f"提取章节号: {chapter_num}")

    # 写入长纲
    if long_part:
        if chapter_num:
            append_to_file(outline_long, long_part, chapter_num)
        else:
            with open(outline_long, "a", encoding="utf-8") as f:
                f.write("\n" + long_part + "\n")
        log("长纲写入完成")
    else:
        log("长纲为空，跳过")

    # 写入短纲
    if short_part:
        with open(outline_short, "a", encoding="utf-8") as f:
            f.write("\n" + short_part + "\n")
        log("短纲写入完成")
    else:
        log("短纲为空，跳过")

    # 可选：删除 temp 文件避免重复处理
    # temp_md.unlink()
    # log("已删除 temp/output.md")

if __name__ == "__main__":
    main()