from serpent.game import Game

from .api.api import PacManAPI

from serpent.utilities import Singleton




class SerpentPacManGame(Game, metaclass=Singleton):

    def __init__(self, **kwargs):
        kwargs["platform"] = "steam"

        kwargs["window_name"] = "ARCADE GAME SERIES: PAC-MAN"

        kwargs["app_id"] = "394160"
        kwargs["app_args"] = None
        

        super().__init__(**kwargs)

        self.api_class = PacManAPI
        self.api_instance = None

    @property
    def screen_regions(self):
        regions = {
            "GAME_REGION": (415, 118, 865, 618), # 450x500
            "SCORE_REGION": (415, 89, 529, 105), # 114x16
            "LIFE_REGION": (420, 620, 536, 644), # 116x24
            "GAME_OVER_REGION": (560, 391, 722, 407), # 162x16
            "GAME_OVER_SECONDARY": (528, 151, 850, 167) # 322x16
        }

        return regions

    @property
    def ocr_presets(self):
        presets = {
            "SAMPLE_PRESET": {
                "extract": {
                    "gradient_size": 1,
                    "closing_size": 1
                },
                "perform": {
                    "scale": 10,
                    "order": 1,
                    "horizontal_closing": 1,
                    "vertical_closing": 1
                }
            }
        }

        return presets
