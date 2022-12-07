# pdf2png

PDFファイルをPNGファイルに1ページ毎に分割して出力を行う

## 使い方

### Python実行

- example.pdfをデフォルト[./output/]に出力  
`$ python pdf2img.py example.pdf`
- example.pdfを[./exam/]に出力  
`$ python pdf2img.py example.pdf exam`

### EXE実行

- example.pdfをデフォルト[./output/]に出力  
`$ pdf2img.exe example.pdf`
- example.pdfを[./exam/]に出力  
`$ pdf2img.exe example.pdf exam`

## 実行ファイルの作成方法

`pdf2png.py`と同ディレクトリで以下のコマンドを実行  
`$ pyinstaller pdf2png.py --onefile`

オプションについては[公式のドキュメント参照](https://pyinstaller.org/en/stable/usage.html#what-to-generate)

## License
[MIT](https://github.com/azisio/pdf2png/blob/main/LICENSE)