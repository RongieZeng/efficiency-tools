import pandas


'''
应用场景：实现类似sql 的联表查询效果，例如： select * from A outer join B on A.Id = B.Id 的效果
'''
df1 = pandas.read_excel("files/source1.xlsx", dtype=str)
df2 = pandas.read_excel("files/source2.xlsx", dtype=str)

# left,right,inner,outer
merge_df = pandas.merge(df1, df2, how="outer", left_on=["Id"], right_on=["Id"])
merge_df.to_excel('files/target.xlsx')