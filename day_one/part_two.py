def count_location_ids_repeated_in_each_list(input_file):
  with open(input_file, 'r') as f:
    lines = f.readlines()
    split_lines = []
    for line in lines:
      line_ids = [id.strip() for id in line.split()]
      split_lines.append(line_ids)
  
  col1 = []
  col2 = []

  for ids in split_lines:
    col1.append(int(ids[0]))
    col2.append(int(ids[1]))
  
  similarity_hashmap = {}

  while col1:
    first_id = col1.pop(0)
    count_second_list = 0
    if first_id in similarity_hashmap:
      continue
    
    for id2 in col2:
      if first_id == id2:
        count_second_list += 1
    
    similarity_hashmap[first_id] = count_second_list
  
  total_similarity = 0

  for id, similarity_score in similarity_hashmap.items():
    total_similarity += id * similarity_score
  
  return total_similarity

print(count_location_ids_repeated_in_each_list('input.txt'))