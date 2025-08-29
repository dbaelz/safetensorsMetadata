
# safetensorsMetadata
Command line tool to extract and print the JSON metadata from a [safetensors](https://github.com/huggingface/safetensors) file.

## Example usage
To extract metadata from a safetensors file:

```
python src/main.py path/to/file.safetensors
```


### Filtering metadata by search string
Filter the metadata output to only show the key/value pairs containing a specific string. This search is case-insensitive and checks both key and value.

Example:
```
python src/main.py path/to/file.safetensors --search author
# or using the short flag
python src/main.py path/to/file.safetensors -s author
```

### Pretty-printing JSON values
Some metadata values may themselves be JSON-encoded strings. By default, these are printed as escaped strings:

```
{
  "training_info": "{\"step\": 1200, \"epoch\": 10}"
}
```

To automatically parse and print such values as unescaped JSON, use the `--pretty` or `-p` flag:

```
python src/main.py path/to/file.safetensors --pretty
# or using the short flag
python src/main.py path/to/file.safetensors -p
```

Output:
```
{
  "training_info": {
    "step": 1200,
    "epoch": 10
  }
}
```

You can combine `--pretty` with `--search` to filter and pretty-print at the same time:

```
python src/main.py path/to/file.safetensors -s info -p
```



## Requirements
- Python 3.8+
- No external dependencies required for basic metadata extraction


## Contribution
Feel free to contribute via pull requests. Please ensure new features are documented and tested.

## License
The project is licensed under the [Apache 2 license](LICENSE).