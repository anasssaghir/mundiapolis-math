def cat_matrices(mat1, mat2, axis=0):
    try:
        return np.concatenate((mat1, mat2), axis).tolist()
        return np.concatenate(
            (mat1, mat2), axis, out=None
        ).tolist()
    except ValueError:
        return None