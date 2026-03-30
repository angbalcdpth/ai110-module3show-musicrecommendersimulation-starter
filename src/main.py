"""
Command line runner for the Music Recommender Simulation.

This file helps you quickly run and test your recommender.

You will implement the functions in recommender.py:
- load_songs
- score_song
- recommend_songs
"""

from recommender import load_songs, recommend_songs


def main() -> None:
    songs = load_songs("data/songs.csv") 


    # Expanded user profile with new features
    user_profile = {
        "favorite_genre": "pop",
        "favorite_mood": "happy",
        "target_energy": 0.80,
        "target_tempo_bpm": 120,
        "target_valence": 0.85,
        "target_danceability": 0.8,
        "target_acousticness": 0.2,
        "target_instrumentalness": 0.1,
        "target_popularity": 60
    }

    recommendations = recommend_songs(user_profile, songs, k=5)

    print("\nTop recommendations (pop/happy profile):\n")
    print("{:<25} {:>8}  {}".format("Title", "Score", "Reasons"))
    print("{:-<25} {:-<8}  {:-<50}".format("", "", ""))

    for song, score, explanation in recommendations:
        # Clean output; wrap explanation if needed.
        print(f"{song['title']:<25} {score:>8.2f}  {explanation}")
    print()


if __name__ == "__main__":
    main()
