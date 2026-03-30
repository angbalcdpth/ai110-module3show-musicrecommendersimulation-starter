from typing import List, Dict, Tuple, Optional
from dataclasses import dataclass

@dataclass
class Song:
    """
    Represents a song and its attributes.
    Required by tests/test_recommender.py
    """
    id: int
    title: str
    artist: str
    genre: str
    mood: str
    energy: float
    tempo_bpm: float
    valence: float
    danceability: float
    acousticness: float

@dataclass
class UserProfile:
    """
    Represents a user's taste preferences.
    Required by tests/test_recommender.py
    """
    favorite_genre: str
    favorite_mood: str
    target_energy: float
    likes_acoustic: bool

class Recommender:
    """
    OOP implementation of the recommendation logic.
    Required by tests/test_recommender.py
    """
    def __init__(self, songs: List[Song]):
        self.songs = songs

    def recommend(self, user: UserProfile, k: int = 5) -> List[Song]:
        # TODO: Implement recommendation logic
        return self.songs[:k]

    def explain_recommendation(self, user: UserProfile, song: Song) -> str:
        # TODO: Implement explanation logic
        return "Explanation placeholder"

def load_songs(csv_path: str) -> List[Dict]:
    """
    Loads songs from a CSV file using Python's csv module.

    Each row is converted to a dictionary and numeric fields are
    converted to floats/ints so future scoring math works correctly.

    Returns:
        List[Dict]: list of song dictionaries with typed values.
    """
    import csv

    songs: List[Dict] = []
    print(f"Loading songs from {csv_path}...")

    with open(csv_path, newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            if not row or all(v == '' for v in row.values()):
                continue

            try:
                song = {
                    'id': int(row['id']),
                    'title': row['title'],
                    'artist': row['artist'],
                    'genre': row['genre'],
                    'mood': row['mood'],
                    'energy': float(row['energy']),
                    'tempo_bpm': float(row['tempo_bpm']),
                    'valence': float(row['valence']),
                    'danceability': float(row['danceability']),
                    'acousticness': float(row['acousticness']),
                    'instrumentalness': float(row.get('instrumentalness', 0.0)),
                    'popularity': int(row.get('popularity', 0))
                }
            except (ValueError, KeyError) as exc:
                raise ValueError(f"Invalid song row in {csv_path}: {row}") from exc

            songs.append(song)

    print(f"Loaded songs: {len(songs)}")
    return songs

def score_song(user_prefs: Dict, song: Dict) -> Tuple[float, List[str]]:
    """
    Scores a single song for the given user preferences and provides reasons.

    Recipe:
    - Genre match: +2.0 points
    - Mood match: +1.0 point
    - Energy similarity: up to +1.5 points using 1.5 * (1 - abs(song_energy - target_energy))
    - Tempo similarity: up to +1.0 points using 1.0 * (1 - abs(song_tempo - target_tempo)/60)
    - Popularity bonus: +0.5 points if popularity > 60

    Returns:
        (score, reasons)
    """
    score = 0.0
    reasons: List[str] = []

    # Genre (experiment: half weight)
    if user_prefs.get('favorite_genre') and song.get('genre'):
        if song['genre'].lower() == user_prefs['favorite_genre'].lower():
            score += 1.0  # changed from 2.0 to 1.0
            reasons.append('genre match (+1.0)')
        else:
            reasons.append('genre mismatch (+0.0)')

    # Mood
    if user_prefs.get('favorite_mood') and song.get('mood'):
        if song['mood'].lower() == user_prefs['favorite_mood'].lower():
            score += 1.0
            reasons.append('mood match (+1.0)')
        else:
            reasons.append('mood mismatch (+0.0)')

    # Energy (experiment: double importance)
    if 'target_energy' in user_prefs and 'energy' in song:
        energy_diff = abs(song['energy'] - float(user_prefs['target_energy']))
        energy_score = max(0.0, 3.0 * (1.0 - energy_diff))  # changed from 1.5 to 3.0
        score += energy_score
        reasons.append(f'energy similarity (+{energy_score:.2f})')

    # Tempo (optional)
    if 'target_tempo_bpm' in user_prefs and 'tempo_bpm' in song:
        tempo_diff = abs(song['tempo_bpm'] - float(user_prefs['target_tempo_bpm']))
        tempo_score = max(0.0, 1.0 * (1.0 - min(tempo_diff, 60.0) / 60.0))
        score += tempo_score
        reasons.append(f'tempo similarity (+{tempo_score:.2f})')

    # Popularity bonus (optional)
    if 'popularity' in song and song['popularity'] > 60:
        score += 0.5
        reasons.append('popularity bonus (+0.5)')

    return score, reasons


def recommend_songs(user_prefs: Dict, songs: List[Dict], k: int = 5) -> List[Tuple[Dict, float, str]]:
    """
    Functional implementation of the recommendation logic.
    Required by src/main.py
    """
    scored = []
    for song in songs:
        score, reasons = score_song(user_prefs, song)
        explanation = '; '.join(reasons)
        scored.append((song, score, explanation))

    scored.sort(key=lambda item: item[1], reverse=True)
    return scored[:k]

