import argparse
import sys
import json


def read_safetensors_metadata(file_path):
    with open(file_path, 'rb') as file:
        header_len_bytes = file.read(8)
        
        if len(header_len_bytes) != 8:
            raise ValueError('File too short to contain a valid safetensors header length.')
        
        header_len = int.from_bytes(header_len_bytes, 'little')
        header_bytes = file.read(header_len)
        
        if len(header_bytes) != header_len:
            raise ValueError('File too short to contain the full safetensors header.')
        
        header = json.loads(header_bytes.decode('utf-8'))
        metadata = header.get('__metadata__', {})
        return metadata


def main():
    parser = argparse.ArgumentParser(description='Read metadata from a safetensors file.')
    parser.add_argument('file', help='Path to the safetensors file')
    args = parser.parse_args()

    try:
        metadata = read_safetensors_metadata(args.file)
        print(json.dumps(metadata, indent=2, ensure_ascii=False))
    except Exception as e:
        print(f'Error: {e}', file=sys.stderr)
        sys.exit(1)


if __name__ == '__main__':
    main()
