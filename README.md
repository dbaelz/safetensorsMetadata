
# safetensorsMetadata
Command line tool to extract and print the JSON metadata from a [safetensors](https://github.com/huggingface/safetensors) file.

## Example usage
To extract metadata from a safetensors file:

```
python main.py path/to/file.safetensors
```

### Filtering metadata by search string
Filter the metadata output to only show the key/value pairs contain a specific string. This search is case-insensitive and checks for key and value.


This example will print only the metadata entries where either the key or value contains "author":
```
python main.py path/to/file.safetensors --search author
# or using the short flag
python main.py path/to/file.safetensors -s author
```


## Requirements
- Python 3.8+
- No external dependencies required for basic metadata extraction

## Contribution
Feel free to contribute via pull requests.

## License
The project is licensed under the [Apache 2 license](LICENSE).