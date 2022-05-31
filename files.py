from ctypes import sizeof
from turtle import clear
import numpy as np
import merger as merge
import pandas as pd


def prepareTeamsAttendanceList(path):
    list = pd.read_excel(path)
    merge.deleteFileRows(list, [0, 1, 2, 3, 4, 5, 6])
    merge.renameFileColumns(list, ['Resumen de la reunión', 'Unnamed: 1', 'Unnamed: 2', 'Unnamed: 3', 'Unnamed: 4', 'Unnamed: 5', 'Unnamed: 6'], [
                            'Nombre completo', 'Hora de unión', 'Hora de salida', 'Duración', 'Correo Institucional', 'Rol', 'UPN'])
    list.to_excel("lista_teams.xlsx")
    print("🟢 Transformed")
    return list


def prepareRegistrationList(xiePath, altPath, datePath):
    xieList = pd.read_excel(xiePath)
    altList = pd.read_excel(altPath)
    dateList = pd.read_excel(datePath)
    dates = dateList.values.tolist()
    prepareAltRegistrationList(altList, dates)
    PrepareXieRegistrationList(xieList, dates)
    list = merge.concatFiles(xieList, altList, [
        'Fecha', 'Pregrados', 'Nombre Participante', 'ID Participante', 'Documento', 'Correo Institucional'])
    list.to_excel("registro.xlsx")
    print("🟢 Transformed")
    return list

def PrepareXieRegistrationList(list, dates):
    dateList = []
    list.dropna(subset=['Nombre Participante'], inplace=True)
    for i in list['Nº Clase'].tolist():
        for j in dates:
            if j[1] == i:
                dateList.append(j[0])
    list['Fecha'] = dateList
        
    
def prepareAltRegistrationList(list, dates):
    dateList = []
    merge.renameFileColumns(list,
                            ['Seleccione la fecha a la cual se desea inscribir', 'Seleccione el programa al que pertenece',
                                'Ingrese su ID de la universidad (Con el 000)', 'Ingrese su número de documento', 'Ingrese su nombre completo', 'Ingrese su correo institucional (con @javeriana.edu.co)'],
                            ['Fecha y Codigo', 'Pregrados', 'ID Participante', 'Documento', 'Nombre Participante', 'Correo Institucional'])
    for i in list['Fecha y Codigo'].tolist():
        split = i.split(" - ")
        for j in dates:
            if j[1] == int(split[1]):
                dateList.append(j[0])
    list['Fecha'] = dateList
        


def prepareFile(path, name):
    list = pd.read_excel(path)
    list.to_excel(name + ".xlsx")
    print("🟢 Transformed")


def checkIfStudentAttendedToTeams(teamsList, registrationList):
    finalList = registrationList
    attendaceList = []
    for i in finalList['Correo Institucional'].tolist():
        if i in teamsList['Correo Institucional'].tolist():
            attendaceList.append("Si")
        else:
            attendaceList.append("No")
    finalList['Teams'] = attendaceList
    finalList.to_excel("final.xlsx")


def checkIfStudentAnsweredSatisfactionForm(formList, registrationList):
    finalList = registrationList
    formsList = []
    for i in finalList['Correo Institucional'].tolist():
        if i in formList['Correo Institucional'].tolist():
            formsList.append("Si")
        else:
            formsList.append("No")
    finalList['Encuesta de satisfacción'] = formsList
    finalList.to_excel("final.xlsx")


def checkIfStudentAnsweredAttendanceForm(formList, registrationList):
    finalList = registrationList
    formsList = []
    for i in finalList['Documento'].tolist():
        if i in formList['Número de documento'].tolist():
            formsList.append("Si")
        else:
            formsList.append("No")
    finalList['Encuesta de asistencia'] = formsList
    finalList.to_excel("final.xlsx")


def finalMerge(registrationPath, teamsPath, attendancePath, satisfactionPath):
    registrationList = pd.read_excel(registrationPath)
    teamsList = pd.read_excel(teamsPath)
    attendanceList = pd.read_excel(attendancePath)
    satisfactionList = pd.read_excel(satisfactionPath)
    checkIfStudentAttendedToTeams(teamsList, registrationList)
    checkIfStudentAnsweredAttendanceForm(attendanceList, registrationList)
    checkIfStudentAnsweredSatisfactionForm(satisfactionList, registrationList)
    print("⚪ Merged")
