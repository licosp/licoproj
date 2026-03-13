import json
import sys

def convert_to_jsonl(input_file, output_file):
    try:
        with open(input_file, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        messages = data.get('messages', [])
        
        with open(output_file, 'w', encoding='utf-8') as out_f:
            for msg in messages:
                # ユーザーの要望に従い、見た目に関する要素(例えば thoughts の description 等)を
                # 削除してミニマムにするか検討。
                # 現状は全てをダンプするが、必要ならここで msg ディクショナリを加工する。
                # 例: if 'thoughts' in msg: del msg['thoughts']
                
                # ミニマム化（tokens と thoughts は巨大になりがちなので削除/簡略化するか？）
                # ユーザーの指示: 「見た目に関する json の文字は削除して、ミニマムにするとか」
                # → 意味を変えずに JSONL 形式のコンパクトな形にする。
                
                out_f.write(json.dumps(msg, ensure_ascii=False) + '\n')
                
        print(f"Successfully converted {len(messages)} messages to {output_file}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python json_to_jsonl.py <input.json> <output.jsonl>")
        sys.exit(1)
    convert_to_jsonl(sys.argv[1], sys.argv[2])
