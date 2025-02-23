
#SNP_Checker_Fluidigm

'This module checks to see if the data file exists and if yes, to import it into the SNP checker xlsx.

Sub Import()
    Dim dataWB As Workbook
    Dim rawDataWS As Worksheet
    Dim dataFilePath As String
    Dim dataRangeE As Range, dataRangeJ As Range
    Dim rawDataRangeA As Range, rawDataRangeB As Range
    
    ' Set the path to the "Data" Excel file.
    dataFilePath = "C:\Users\Data.csv" ' Replace this with actual file path.
    
    ' Check if the "Data" file exists
    If Dir(dataFilePath) = "" Then
        MsgBox "Data file not found. Please check the file path and if correctly named.", vbExclamation
        Exit Sub
    End If
    
    ' Open the "Data" workbook.
    Set dataWB = Workbooks.Open(dataFilePath)
    
    ' Set the data ranges in the "Data" workbook.
    Set dataRangeE = dataWB.Worksheets("Data").Range("E17:E4624")
    Set dataRangeJ = dataWB.Worksheets("Data").Range("J17:J4624")
    
    ' Set the "Raw_data" worksheet in the "SNP checker" workbook.
    Set rawDataWS = ThisWorkbook.Worksheets("Raw_data")
    
    ' Set the destination ranges in the "Raw_data" worksheet.
    Set rawDataRangeA = rawDataWS.Range("A1")
    Set rawDataRangeB = rawDataWS.Range("B1")
    
    ' Copy data from "Data" workbook and paste it into the "Raw_data" worksheet.
    rawDataRangeA.Resize(dataRangeE.Rows.Count, 1).Value = dataRangeE.Value
    rawDataRangeB.Resize(dataRangeJ.Rows.Count, 1).Value = dataRangeJ.Value
    
    ' Close the "Data" workbook without saving changes.
    dataWB.Close SaveChanges:=False
    
    MsgBox "Data imported successfully!", vbInformation
End Sub

'This module concatanates the alleles in the 24 SNPs per individual.

Sub CombineAlleles()
    Dim ws As Worksheet
    Dim lastRow As Long
    Dim nameCol As Range, allelesCol As Range, outputCol As Range
    Dim nameCell As Range, allelesCell As Range, outputCell As Range
    Dim sentence As String
    Dim isFirstOccurrence As Boolean
    Dim firstName As String ' Variable to store the first name in the group
    Dim prevSentence As String ' Variable to store the previous sentence
    
    ' Change the sheet name (Sheet1) to your actual sheet name where the data is located.
    Set ws = ThisWorkbook.Worksheets("Sheet1")
    
    ' Assuming "Name" is in column A, "Alleles" is in column B, and the output should be in column C.
    ' If your columns are different, adjust the column letters accordingly.
    Set nameCol = ws.Range("A2:A" & ws.Cells(ws.Rows.Count, "A").End(xlUp).Row)
    Set allelesCol = ws.Range("B2:B" & ws.Cells(ws.Rows.Count, "B").End(xlUp).Row)
    Set outputCol = ws.Range("C2:C" & ws.Cells(ws.Rows.Count, "C").End(xlUp).Row)
    
    For Each nameCell In nameCol
        If nameCell.Value <> firstName Then
            sentence = ""
            For Each allelesCell In nameCell.Resize(24, 1).Offset(0, 1).Cells
                ' Assuming the alleles are only letters. If there are other characters, you can modify the pattern.
                sentence = sentence & " " & Application.Trim(allelesCell.Value)
            Next allelesCell
            ' Remove the leading space from the sentence.
            sentence = Application.Trim(sentence)
            firstName = nameCell.Value ' Store the first name in the group
        End If
        ' Copy the sentence to the first cell in the output column.
        nameCell.Offset(0, 2).Value = sentence
        
        ' Check if the current sentence matches the previous sentence.
        If sentence = prevSentence Then
            ' If they match, clear the value for the current cell.
            nameCell.Offset(0, 2).Value = ""
        End If
        ' Store the current sentence in prevSentence for comparison in the next loop.
        prevSentence = sentence
    Next nameCell
End Sub

