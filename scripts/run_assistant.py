import subprocess

from dotenv import dotenv_values

envs = dotenv_values()
envs_cmd = " ".join([f"{key}={value}" for key, value in envs.items()])


if __name__ == "__main__":
    cmd = f"{envs_cmd} streamlit run src/front/main.py"
    subprocess.run(cmd, shell=True)
