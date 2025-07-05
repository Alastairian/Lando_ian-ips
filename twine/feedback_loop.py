from twine.logos_core import LogosCore
from twine.pathos_core import PathosCore

class TwineCognition:
    def __init__(self, num_units: int, input_dim: int, aspect_list: list):
        self.logos = LogosCore(num_units, input_dim, aspect_list)
        self.pathos = PathosCore(num_units, input_dim, aspect_list)

    def process(self, input_data: list) -> list:
        pathos_markers = self.pathos.process(input_data)
        # Use Pathos output to bias Logos processing
        logos_result = self.logos.process(input_data + [sum(map(sum, pathos_markers))])
        # Feedback: update Pathos with Logos error or uncertainty signals (not yet implemented)
        return logos_result