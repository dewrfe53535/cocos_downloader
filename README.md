# cocos_downloader

由于没找到通用的下载 cocos2d 网页游戏资源的工具而自己造的轮子。没有兜底等错误处理，使用时需小心。   
没有按照官方实现，但应该能下大部分内容。
 

## 安装

```console
pip install git+https://github.com/dewrfe53535/cocos-downloader
```

## 使用

### 基本下载

```python
from cocos2d_downloader.downloader import assetDownloader

config_dict = {
    "downloader_assetroot": "https://example.com/", # 清单的根路径
    "downloader_weburl": "", # 旧版兼容，不填
    "downloader_threadnum": 20, # 线程数
    "downloader_savepath": "resource/game", # 下载资源保存位置
    "asset_baseurl": "https://example.com/assets" # 资源的根路径
}


downloader = assetDownloader(config_dict)
settings_jsonUrl = 'https://example.com/src/settings.00000.json' # 总清单位置
jsondata =  requests.get(settings_jsonUrl).json()
downloader.manifestOfmanifestData = jsondata['assets']['bundleVers'] # 总清单字典
# 子项目清单链接格式
downloader.jsurl = 'assets/{typename}/index.{version}.js' 
downloader.configurl = 'assets/{typename}/config.{version}.json'

downloader.downloadAllManifest() # 下载全部清单
downloader.downloadAllFromManifest() # 下载全部资源文件
```

### 自定义资源解密

```python
def decrypt(url,path,data):
    '''
    path为预期保存的本地路径
    '''
    ...
    return True # 若返回True则原函数不做接下来的保存处理
downloader.downloadCallback = decrypt
```

### 清单

  可以继承并重写 `cocos_downloader.parser.ManifestJson` 中的 `convertInfoToUrl` 来实现自定义格式下载链接导出

```python
downloader.customManifestJson = ...
```

```python
res:ManifestJson  = ManifestJson('resources',downloader.manifestData['resources']) # 加载清单
res.mapExt() # 根据清单设置每一项扩展名
# 根据import设置每一项扩展名
downloader.MTdownloadAndSetimport(res,res.getAllpackDownloadUrl())
downloader.MTdownloadAndSetimport(res, res.getAllINDimportDownloadUrl())
res.setRealPaths() # 根据清单中提供的真实地址设置每一项 
res.assetList # 清单中每一项信息的dataclass 
```

## License

`cocos-downloader` is distributed under the terms of the [MIT](https://spdx.org/licenses/MIT.html) license.
