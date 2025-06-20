class ScaleImage:
    def scale(self, image:str, width:int, height:int)->str:
        return f"Image {image} scaled to {width}x{height}"
    
class AdjustColor:
    def change_color(self, image:str, mode: str) -> str:
        return f"Image {image} color mode change to {mode}"
    
class CompressImage:
    def compress(self, image:str, quality: int) -> str:
        return f"Image {image} compressed to quality {quality}%"
    
class GraphicsFacade:
    def __init__(self) -> None:
        self.scaler = ScaleImage()
        self.color_adjuster = AdjustColor()
        self.compressor = CompressImage()

    def process_the_image(self, image:str, width: int, height:int, color_mode: str, quality : int) -> str:
        results = []
        results.append(self.scaler.scale(image, width,height))
        results.append(self.color_adjuster.change_color(image, color_mode))
        results.append(self.compressor.compress(image, quality))
        return "\n".join(results)
    

def main():
    image = "random.img"
    editor = GraphicsFacade()
    result = editor.process_the_image(image, width=200, height=200, color_mode="RGB", quality=90)
    print(result)

if __name__ == "__main__":
    main()