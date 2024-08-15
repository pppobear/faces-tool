def get_all_ids(old_tab_faces_data: dict) -> set[int]:
    return set(face['id'] for face in old_tab_faces_data['faces'])
