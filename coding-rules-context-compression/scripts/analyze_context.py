#!/usr/bin/env python3
"""
Context Usage Analyzer
Estimates token usage from conversation history
"""

import json
import sys
from pathlib import Path

def estimate_tokens(text):
    """Rough token estimation: ~4 chars per token"""
    return len(text) // 4

def analyze_conversation(conversation_file):
    """Analyze a conversation JSONL file"""
    
    total_tokens = 0
    message_count = 0
    tool_calls = 0
    large_responses = []
    
    with open(conversation_file, 'r', encoding='utf-8') as f:
        for line in f:
            try:
                msg = json.loads(line)
                message_count += 1
                
                # Count tokens in message content
                if 'message' in msg and 'content' in msg['message']:
                    content = json.dumps(msg['message']['content'])
                    tokens = estimate_tokens(content)
                    total_tokens += tokens
                    
                    # Track large responses
                    if tokens > 5000:
                        large_responses.append({
                            'index': message_count,
                            'tokens': tokens,
                            'role': msg.get('role', 'unknown')
                        })
                    
                    # Count tool calls
                    if isinstance(msg['message']['content'], list):
                        for item in msg['message']['content']:
                            if isinstance(item, dict) and item.get('type') == 'tool_use':
                                tool_calls += 1
            except:
                continue
    
    return {
        'total_tokens': total_tokens,
        'message_count': message_count,
        'tool_calls': tool_calls,
        'large_responses': large_responses,
        'avg_tokens_per_message': total_tokens // message_count if message_count > 0 else 0
    }

def main():
    if len(sys.argv) < 2:
        print("Usage: python analyze_context.py <conversation.jsonl>")
        sys.exit(1)
    
    conversation_file = sys.argv[1]
    
    if not Path(conversation_file).exists():
        print(f"Error: File not found: {conversation_file}")
        sys.exit(1)
    
    print("=== Context Usage Analysis ===\n")
    
    stats = analyze_conversation(conversation_file)
    
    print(f"Total Messages: {stats['message_count']}")
    print(f"Tool Calls: {stats['tool_calls']}")
    print(f"Estimated Tokens: {stats['total_tokens']:,}")
    print(f"Avg Tokens/Message: {stats['avg_tokens_per_message']:,}")
    
    # Capacity warning
    capacity = 200000  # typical context window
    usage_pct = (stats['total_tokens'] / capacity) * 100
    print(f"\nCapacity Usage: {usage_pct:.1f}%")
    
    if usage_pct > 70:
        print("⚠️  WARNING: Context usage >70%, consider compression")
    elif usage_pct > 90:
        print("🔴 CRITICAL: Context usage >90%, compression required!")
    else:
        print("✅ Context usage healthy")
    
    # Large responses
    if stats['large_responses']:
        print(f"\n=== Large Responses (>5K tokens) ===")
        for resp in stats['large_responses'][:5]:
            print(f"  Message #{resp['index']}: {resp['tokens']:,} tokens ({resp['role']})")

if __name__ == '__main__':
    main()
