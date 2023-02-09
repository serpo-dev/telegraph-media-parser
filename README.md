

# telegraph-media-parser

  

It's a simple tool for parse images and videos from articles on [telegra.ph](https://telegra.ph/). Powered by Python 3. Running from the CLI.

  

### Installation and use

  

Before launching you must make sure that `pip` and `python3` are installed on your device globally.

  

1. In the root folder of the project run the command:

  
```sh
pip install  -r  requirements.txt
```

  

2. Insert links in the file `input.txt`. Each link must start on a new line, for example:

  

```sh
https://telegra.ph/article1
https://telegra.ph/article2
...
```

  

3. Then run the command:

  

```sh
python main.py
```

  

You can specify what you exactly want to save by these flags:


-  `-img` or `--images` ,
-   `-video` or `--videos` .

By the default, it downloads a both.

  

4. The media is saving in the `downloads/` folder that automatically creates in the root directory.

  

```
telegra.ph-media-parser
│
├──  downloads/
│      └── article1/...
│      └── article2/...
│      └── ... 
└── main.py
└── input.txt
└── requirements.txt
```