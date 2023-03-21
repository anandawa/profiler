from pathlib import Path
import os
import pandas as pd
from ydata_profiling import ProfileReport

PROFILE_RESULT_DIR = './profile_results'

def profile(inputfile: str):
    print(f'profiling:{inputfile}')

    df_input = pd.read_csv(inputfile, sep = None)
    filename = os.path.basename(inputfile)
    profile = ProfileReport(df_input, title=filename)

    result_location = f'{PROFILE_RESULT_DIR}/{filename}'
    profile.to_file(result_location)

    print(f'profiling result location:{result_location}')

    profile_id = Path(result_location).stem
    return profile_id