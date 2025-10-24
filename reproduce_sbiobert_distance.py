import argparse
from sentence_transformers import SentenceTransformer
import numpy as np


def get_model_SBioBERT():
    print("Loading S-BioBERT SentenceTransformer model...")
    return SentenceTransformer('pritamdeka/S-BioBert-snli-multinli-stsb')


def main():
    # Parse command-line arguments
    parser = argparse.ArgumentParser(description="Reproduce SBioBERT semantic distance calculation.")
    parser.add_argument("--title", type=str, required=True, help="Title text")
    parser.add_argument("--abstract", type=str, required=True, help="Abstract text")
    parser.add_argument("--query", type=str, required=True, help="Query text for comparison")
    args = parser.parse_args()

    model = get_model_SBioBERT()

    # Combine title and abstract
    stored_text = f"{args.title} {args.abstract}"
    stored_embedding = model.encode(
        stored_text, batch_size=32, convert_to_numpy=True, normalize_embeddings=True
    ).astype(np.float32)

    query_embedding = model.encode(
        args.query, convert_to_numpy=True, normalize_embeddings=True
    ).astype(np.float32).reshape(1, -1)

    # Flatten and compute L2 distance
    stored_vec = np.asarray(stored_embedding).astype(np.float32).reshape(-1)
    query_vec = np.asarray(query_embedding).astype(np.float32).reshape(-1)

    l2_distance = float(np.sum((stored_vec - query_vec) ** 2))

    print("\n" + "=" * 80)
    print(f"Title: {args.title}")
    print(f"Query: '{args.query}'")
    print(f"L2 Distance: {l2_distance:.3f}")
    print("=" * 80)


if __name__ == "__main__":
    main()
