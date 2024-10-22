from cog import BasePredictor, Input, Path
import subprocess
import os

class Predictor(BasePredictor):
    def setup(self):
        self.model_dir = "/models/mochi_preview"
        # Assuming weights are manually downloaded and placed in the correct directory

    def predict(
        self,
        prompt: str = Input(description="Video prompt"),
        seed: int = Input(description="Seed for generation reproducibility"),
        cfg_scale: float = Input(description="CFG scale for controlling randomness")
    ) -> Path:
        video_path = "/tmp/generated_video.mp4"
        command = [
            "python3", "-m", "mochi_preview.infer",
            "--prompt", prompt,
            "--seed", str(seed),
            "--cfg-scale", str(cfg_scale),
            "--model_dir", self.model_dir,
            "--output", video_path
        ]
        # Run the command
        subprocess.run(command, check=True)
        return Path(video_path)
