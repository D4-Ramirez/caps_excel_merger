import pandas as pd


def createLeftJoinFile(mainFilePath, addFilePath, on):
    mainFile = pd.read_excel(mainFilePath)
    addFile = pd.read_excel(addFilePath)
    left_join_df = mainFile.merge(addFile, how="left", on=on)
    left_join_df.to_excel("LeftJoin.xlsx")


def createInnerJoinFile(mainFilePath, addFilePath, on):
    mainFile = pd.read_excel(mainFilePath)
    addFile = pd.read_excel(addFilePath)
    inner_join_df = mainFile.merge(addFile, how="inner", on=on)
    inner_join_df.to_excel("InnerJoin.xlsx")


def createRightJoinFile(mainFilePath, addFilePath, on):
    mainFile = pd.read_excel(mainFilePath)
    addFile = pd.read_excel(addFilePath)
    right_join_df = mainFile.merge(addFile, how="right", on=on)
    right_join_df.to_excel("RightJoin.xlsx")


def createOuterJoinFile(mainFilePath, addFilePath, on):
    mainFile = pd.read_excel(mainFilePath)
    addFile = pd.read_excel(addFilePath)
    outer_join_df = mainFile.merge(addFile, how="outer", on=on)
    outer_join_df.to_excel("OuterJoin.xlsx")


def concatFiles(mainFile, addFile, columns):
    return pd.concat([mainFile[columns], addFile[columns]])


def getFileColumns(file):
    return file.columns


def renameFileColumns(file, columnName, newColumnName):
    for i in range(len(columnName)):
        file.rename(
            columns={columnName[i]: newColumnName[i]}, inplace=True)


def deleteFileRows(file, labels):
    file.drop(labels, axis=0, inplace=True)
