example1 = Label(root, text="Top left column")
example1.grid(row=0, column=0)
#Or
example2 = Label(root, text="Middle right colum") .grid(row=1, column=1)

#ColumnSpan
example3 = Label(root, text="Bottom Row")
example3.grid(row=2, columnspan=2)

grids = [[0] * gridSize for _ in range(gridSize)]