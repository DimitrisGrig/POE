from sentence_transformers import SentenceTransformer
import numpy as np


def get_model_SBioBERT():
    print("Loading S-BioBert SentenceTransformer model...")
    return SentenceTransformer('pritamdeka/S-BioBert-snli-multinli-stsb')


def main():
    model = get_model_SBioBERT()

    title = "Smoking status impacts microRNA mediated prognosis and lung adenocarcinoma biology"

    abstract = """
        Background: Cigarette smoke is associated with the majority of lung cancers: however, 25% of lung cancer patients are non-smokers, and half of all newly diagnosed lung cancer patients are former smokers. Lung tumors exhibit distinct epidemiological, clinical, pathological, and molecular features depending on smoking status, suggesting divergent mechanisms underlie tumorigenesis in smokers and non-smokers. MicroRNAs (miRNAs) are integral contributors to tumorigenesis and mediate biological responses to smoking. Based on the hypothesis that smoking-specific miRNA differences in lung adenocarcinomas reflect distinct tumorigenic processes selected by different smoking and non-smoking environments, we investigated the contribution of miRNA disruption to lung tumor biology and patient outcome in the context of smoking status.
        Methods: We applied a whole transcriptome sequencing based approach to interrogate miRNA levels in 94 patient-matched lung adenocarcinoma and non-malignant lung parenchymal tissue pairs from current, former and never smokers.
        Results: We discovered novel and distinct smoking status-specific patterns of miRNA and miRNA-mediated gene networks, and identified miRNAs that were prognostically significant in a smoking dependent manner. Conclusions: We conclude that miRNAs disrupted in a smoking status-dependent manner affect distinct cellular pathways and differentially influence lung cancer patient prognosis in current, former and never smokers. Our findings may represent promising biologically relevant markers for lung cancer prognosis or therapeutic intervention.
        """

    stored_text = f"{title} {abstract}"
    stored_embedding = model.encode(stored_text, batch_size=32, convert_to_numpy=True, normalize_embeddings=True).astype(np.float32)


    comparison_query = "Lung cancer"
    query_embedding = model.encode(comparison_query, convert_to_numpy=True, normalize_embeddings=True).astype(np.float32).reshape(1, -1)

    stored_vec = np.asarray(stored_embedding).astype(np.float32).reshape(-1)
    query_vec = np.asarray(query_embedding).astype(np.float32).reshape(-1)

    l2_distance = float(np.sum((stored_vec - query_vec) ** 2))

    print("\n" + "="*80)
    print(f"Comparison query: '{comparison_query}'")
    print(f"L2 distance: {l2_distance:.3f}")
    print("="*80)

if __name__ == "__main__":
    main()
