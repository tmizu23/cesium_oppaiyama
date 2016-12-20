cesium_oppaiyama
====================

この記事に関連するデータです。
http://d.hatena.ne.jp/tmizu23/20161220

画像は、常識の範囲でご自由にお使いください。

## markerxml2gcptxt.pyについて

PhotoScanからエクスポートしたmarker.xmlをOpenDroneMap用にgcp_list.txtに変換するプログラムです。投影法は、自分で書き換えてください。(PhotoScanがあるなら、そのままPhotoScanで処理すればいいじゃない？というのは、その通りです。)
````
python markerxml2gcptxt.py > gcp_list.txt
````
