# Copyright (c) 2024, NVIDIA CORPORATION.

from pylibcudf.column import Column

def edit_distance(input: Column, targets: Column) -> Column: ...
def edit_distance_matrix(input: Column) -> Column: ...