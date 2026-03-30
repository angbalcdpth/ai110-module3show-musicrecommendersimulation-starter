"""
Command line runner for the Music Recommender Simulation.

This file helps you quickly run and test your recommender.

You will implement the functions in recommender.py:
- load_songs
- score_song
- recommend_songs
"""

from recommender import load_songs, recommend_songs


def print_recommendations(label: str, profile: dict, songs: list, k: int = 5) -> None:
    recommendations = recommend_songs(profile, songs, k=k)
    print(f"\nTop recommendations ({label}):\n")
    print("{:<25} {:>8}  {}".format("Title", "Score", "Reasons"))
    print("{:-<25} {:-<8}  {:-<50}".format("", "", ""))

    for song, score, explanation in recommendations:
        print(f"{song['title']:<25} {score:>8.2f}  {explanation}")
    print()


def main() -> None:
    songs = load_songs("data/songs.csv")

    # Profile 1: High-Energy Pop
    high_energy_pop = {
        "favorite_genre": "pop",
        "favorite_mood": "energetic",
        "target_energy": 0.95,
        "target_tempo_bpm": 130,
        "target_valence": 0.90,
        "target_danceability": 0.92,
        "target_acousticness": 0.05,
        "target_instrumentalness": 0.02,
        "target_popularity": 80
    }

    # Profile 2: Chill Lofi
    chill_lofi = {
        "favorite_genre": "lofi",
        "favorite_mood": "relaxed",
        "target_energy": 0.25,
        "target_tempo_bpm": 70,
        "target_valence": 0.50,
        "target_danceability": 0.30,
        "target_acousticness": 0.60,
        "target_instrumentalness": 0.85,
        "target_popularity": 40
    }

    # Profile 3: Deep Intense Rock
    deep_rock = {
        "favorite_genre": "rock",
        "favorite_mood": "intense",
        "target_energy": 0.88,
        "target_tempo_bpm": 110,
        "target_valence": 0.40,
        "target_danceability": 0.55,
        "target_acousticness": 0.15,
        "target_instrumentalness": 0.30,
        "target_popularity": 65
    }

    # Adversarial/ege case profile: conflicting preferences
    conflicting_profile = {
        "favorite_genre": "jazz",
        "favorite_mood": "sad",
        "target_energy": 0.90,
        "target_tempo_bpm": 150,
        "target_valence": 0.10,
        "target_danceability": 0.95,
        "target_acousticness": 0.10,
        "target_instrumentalness": 0.00,
        "target_popularity": 10
    }

    print_recommendations("High-Energy Pop", high_energy_pop, songs)
    print_recommendations("Chill Lofi", chill_lofi, songs)
    print_recommendations("Deep Intense Rock", deep_rock, songs)
    print_recommendations("Adversarial Conflicting", conflicting_profile, songs)


if __name__ == "__main__":
    main()
