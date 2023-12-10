import pathlib

SAMPLE_DIR: pathlib.Path = pathlib.Path('sample')
CHALLENGE_DIR: pathlib.Path = pathlib.Path('challenge')

def get_sample(day:int, part:str='', option:int=0) -> str:
    sample_pattern = f'day{day:02d}{part.lower()}*.txt'

    samples = list(SAMPLE_DIR.glob(sample_pattern))

    if len(samples) == 0:
        raise FileNotFoundError(f'No sample input found for day {day} in {SAMPLE_DIR}')

    if option >= len(samples):
        raise FileNotFoundError(
            '\n'.join(
                [f'Too few samples found for day {day}',
                f'  samples found: {len(samples)}'
                f'  sample requested: {option}',]
            )
        )

    return sorted(samples)[option].read_text()

def get_challenge(day:int) -> str:
    challenge = next(CHALLENGE_DIR.glob(f'day{day:02d}*.txt'), None)
    
    if challenge is None:
        raise FileNotFoundError(f'No challenge input found for day {day} in {CHALLENGE_DIR}')

    return challenge.read_text()