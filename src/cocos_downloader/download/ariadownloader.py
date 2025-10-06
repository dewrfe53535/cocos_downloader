import aria2p
from ..config import Config

class aria2downloader:
    def __init__(self) -> None:
        self.aria2 = aria2p.API(
            aria2p.Client(
                host="http://localhost",
                port=16800,
                secret=""
            ))
        self.aria2option = aria2p.Options(self.aria2, {})
        self.aria2option.user_agent = Config.user_agent
        self.aria2option.allow_overwrite = True
        self.aria2option.auto_file_renaming = False
        self.aria2option.continue_downloads = False
        
    def downloadfile(self,url,localPath):
        pass
        
    def downloadfiles(self,filedict:dict[str:str]):
        '''
        filedict:url->download path
        '''
        pass

    def isAllCompleted(self):
        return not self.aria2.get_stats().num_active