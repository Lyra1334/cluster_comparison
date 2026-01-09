Scripts to be used with ABMHub's doc-zsl to analize how similar two clusters are.

How to use:
<ul>
  <li>Use <code>gerar_embeds.py</code> to generate embedding csvs for each cluster to be compared. 
    <ul>
      <li> The flag <code>--root folder</code> defines where the code will look for clusters</li>
      <li> The flag <code>--csv_dest</code> defines where the code will write the embeddings</li>
      <li> The flag <code>--model_path</code> defines the pre-trained model to be used</li>
      <li> The flag <code>--calculate_distances_path</code> defines the position of the script used to generate the embeddings</li>
    </ul>
  </li>
  <li>Use <code>calc_centroides.py</code> to calculate the position of each cluster's centroid and compare it to all other clusters.
    <ul>
      <li> The flag <code>--embeds_folder</code> defines where the code will look for the csvs containing the clusters' embeddings.</li>
      <li> The flag <code>--comparison_dest</code> defines where the code will write the comparison file.</li>
    </ul>
  </li>
</ul>
