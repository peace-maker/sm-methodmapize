#!/usr/bin/python
# Methodmapizer for SourcePawn 1.7+
# Replaces all native calls with their equivalent methodmap call.
# By Peace-Maker
# Version 1.0

import sys
import re
import os.path

if len(sys.argv) < 2:
	print('Give at least one file to methodmapize: file1.sp file2.sp ...')
	sys.exit(1)

# Run through all passed files
for i in range(1, len(sys.argv)):
	if not os.path.isfile(sys.argv[i]):
		print('File not found: {}'.format(sys.argv[i]))
		continue

	code = ''
	with open(sys.argv[i], 'r') as f:
		code = f.read()

		print('Methodmapizing {}'.format(sys.argv[i]))

		# AdminId
		code = re.sub(r"BindAdminIdentity\s*\(\s*([^\,]+)\s*,\s*", r"\1.BindIdentity(", code)
		code = re.sub(r"CanAdminTarget\s*\(\s*([^\,]+)\s*,\s*", r"\1.CanTarget(", code)
		code = re.sub(r"GetAdminFlags\s*\(\s*([^\,]+)\s*,\s*", r"\1.GetFlags(", code)
		code = re.sub(r"GetAdminGroup\s*\(\s*([^\,]+)\s*,\s*", r"\1.GetGroup(", code)
		code = re.sub(r"GetAdminPassword\s*\(\s*([^\,]+)\s*,\s*", r"\1.GetPassword(", code)
		code = re.sub(r"GetAdminFlag\s*\(\s*([^\,]+)\s*,\s*", r"\1.HasFlag(", code)
		code = re.sub(r"AdminInheritGroup\s*\(\s*([^\,]+)\s*,\s*", r"\1.InheritGroup(", code)
		code = re.sub(r"SetAdminPassword\s*\(\s*([^\,]+)\s*,\s*", r"\1.SetPassword(", code)
		code = re.sub(r"GetAdminGroupCount\s*\(\s*([^\)]+)\s*\)", r"\1\.GroupCount", code)
		code = re.sub(r"GetAdminImmunityLevel\s*\(\s*([^\)]+)\s*\)", r"\1\.ImmunityLevel", code)
		code = re.sub(r"SetAdminImmunityLevel\s*\(\s*([^\,]+)\s*,\s*([^\)]+)\s*\)", r"\1.ImmunityLevel = \2", code)

		# GroupId
		code = re.sub(r"AddAdmGroupCmdOverride\s*\(\s*([^\,]+)\s*,\s*", r"\1.AddCommandOverride(", code)
		code = re.sub(r"SetAdmGroupImmuneFrom\s*\(\s*([^\,]+)\s*,\s*", r"\1.AddGroupImmunity(", code)
		code = re.sub(r"GetAdmGroupCmdOverride\s*\(\s*([^\,]+)\s*,\s*", r"\1.GetCommandOverride(", code)
		code = re.sub(r"GetAdmGroupAddFlags\s*\(\s*([^\,]+)\s*,\s*", r"\1.GetFlags(", code)
		code = re.sub(r"GetAdmGroupImmunity\s*\(\s*([^\,]+)\s*,\s*", r"\1.GetGroupImmunity(", code)
		code = re.sub(r"GetAdmGroupAddFlag\s*\(\s*([^\,]+)\s*,\s*", r"\1.HasFlag(", code)
		code = re.sub(r"SetAdmGroupAddFlag\s*\(\s*([^\,]+)\s*,\s*", r"\1.SetFlag(", code)
		code = re.sub(r"GetAdmGroupImmuneCount\s*\(\s*([^\)]+)\s*\)", r"\1\.GroupImmunitiesCount", code)
		code = re.sub(r"GetAdmGroupImmunityLevel\s*\(\s*([^\)]+)\s*\)", r"\1\.ImmunityLevel", code)
		code = re.sub(r"SetAdmGroupImmunityLevel\s*\(\s*([^\,]+)\s*,\s*([^\)]+)\s*\)", r"\1.ImmunityLevel = \2", code)

		# ArrayList
		code = re.sub(r"ClearArray\s*\(\s*([^\)]+)\s*\)", r"\1.Clear()", code)
		code = re.sub(r"CloneArray\s*\(\s*([^\)]+)\s*\)", r"\1.Clone()", code)
		code = re.sub(r"CreateArray\s*\(\s*([^\)]*)\s*\)", r"new ArrayList(\1)", code)
		code = re.sub(r"FindStringInArray\s*\(\s*([^\,]+)\s*,\s*", r"\1.FindString(", code)
		code = re.sub(r"FindValueInArray\s*\(\s*([^\,]+)\s*,\s*", r"\1.FindValue(", code)
		code = re.sub(r"GetArrayArray\s*\(\s*([^\,]+)\s*,\s*", r"\1.GetArray(", code)
		code = re.sub(r"GetArrayCell\s*\(\s*([^\,]+)\s*,\s*", r"\1.Get(", code)
		code = re.sub(r"GetArraySize\s*\(\s*([^\)]+)\s*\)", r"\1\.Length", code)
		code = re.sub(r"GetArrayString\s*\(\s*([^\,]+)\s*,\s*", r"\1.GetString(", code)
		code = re.sub(r"PushArrayArray\s*\(\s*([^\,]+)\s*,\s*", r"\1.PushArray(", code)
		code = re.sub(r"PushArrayCell\s*\(\s*([^\,]+)\s*,\s*", r"\1.Push(", code)
		code = re.sub(r"PushArrayString\s*\(\s*([^\,]+)\s*,\s*", r"\1.PushString(", code)
		code = re.sub(r"RemoveFromArray\s*\(\s*([^\,]+)\s*,\s*", r"\1.Erase(", code)
		code = re.sub(r"ResizeArray\s*\(\s*([^\,]+)\s*,\s*", r"\1.Resize(", code)
		code = re.sub(r"SetArrayArray\s*\(\s*([^\,]+)\s*,\s*", r"\1.SetArray(", code)
		code = re.sub(r"SetArrayCell\s*\(\s*([^\,]+)\s*,\s*", r"\1.Set(", code)
		code = re.sub(r"SetArrayString\s*\(\s*([^\,]+)\s*,\s*", r"\1.SetString(", code)
		code = re.sub(r"ShiftArrayUp\s*\(\s*([^\,]+)\s*,\s*", r"\1.ShiftUp(", code)
		code = re.sub(r"SwapArrayItems\s*\(\s*([^\,]+)\s*,\s*", r"\1.SwapAt(", code)

		# ArrayStack
		code = re.sub(r"CreateStack\s*\(\s*([^\)]*)\s*\)", r"new ArrayStack(\1)", code)
		code = re.sub(r"IsStackEmpty\s*\(\s*([^\)]+)\s*\)", r"\1.Empty", code)
		code = re.sub(r"PopStackArray\s*\(\s*([^\,]+)\s*,\s*", r"\1.PopArray(", code)
		code = re.sub(r"PopStackCell\s*\(\s*([^\,]+)\s*,\s*", r"\1.Pop(", code)
		code = re.sub(r"PopStackString\s*\(\s*([^\,]+)\s*,\s*", r"\1.PopString(", code)
		code = re.sub(r"PushStackArray\s*\(\s*([^\,]+)\s*,\s*", r"\1.PushArray(", code)
		code = re.sub(r"PushStackCell\s*\(\s*([^\,]+)\s*,\s*", r"\1.Push(", code)
		code = re.sub(r"PushStackString\s*\(\s*([^\,]+)\s*,\s*", r"\1.PushString(", code)

		# StringMap
		code = re.sub(r"CreateTrie\s*\(\s*\)", r"new StringMap()", code)
		code = re.sub(r"GetTrieSize\s*\(\s*([^\)]+)\s*\)", r"\1.Size", code)
		code = re.sub(r"ClearTrie\s*\(\s*([^\)]+)\s*\)", r"\1.Clear()", code)
		code = re.sub(r"GetTrieString\s*\(\s*([^\,]+)\s*,\s*", r"\1.GetString(", code)
		code = re.sub(r"SetTrieString\s*\(\s*([^\,]+)\s*,\s*", r"\1.SetString(", code)
		code = re.sub(r"GetTrieValue\s*\(\s*([^\,]+)\s*,\s*", r"\1.GetValue(", code)
		code = re.sub(r"SetTrieValue\s*\(\s*([^\,]+)\s*,\s*", r"\1.SetValue(", code)
		code = re.sub(r"GetTrieArray\s*\(\s*([^\,]+)\s*,\s*", r"\1.GetArray(", code)
		code = re.sub(r"SetTrieArray\s*\(\s*([^\,]+)\s*,\s*", r"\1.SetArray(", code)
		code = re.sub(r"RemoveFromTrie\s*\(\s*([^\,]+)\s*,\s*", r"\1.Remove(", code)

		# StringMapSnapshot
		code = re.sub(r"CreateTrieSnapshot\s*\(\s*([^\)]+)\s*\)", r"\1.Snapshot()", code)
		code = re.sub(r"TrieSnapshotKeyBufferSize\s*\(\s*([^\,]+)\s*,\s*", r"\1.KeyBufferSize(", code)
		code = re.sub(r"GetTrieSnapshotKey\s*\(\s*([^\,]+)\s*,\s*", r"\1.GetKey(", code)
		code = re.sub(r"TrieSnapshotLength\s*\(\s*([^\)]+)\s*\)", r"\1.Length", code)

		# TODO
		# BfRead
		# BfWrite

		# ConVar
		code = re.sub(r"GetConVarBool\s*\(\s*([^\)]+)\s*\)", r"\1.BoolValue", code)
		code = re.sub(r"GetConVarBounds\s*\(\s*([^\,]+)\s*,\s*", r"\1.GetBounds(", code)
		code = re.sub(r"GetConVarDefault\s*\(\s*([^\,]+)\s*,\s*", r"\1.GetDefault(", code)
		code = re.sub(r"GetConVarFlags\s*\(\s*([^\)]+)\s*\)", r"\1.Flags", code)
		code = re.sub(r"GetConVarFloat\s*\(\s*([^\)]+)\s*\)", r"\1.FloatValue", code)
		code = re.sub(r"GetConVarInt\s*\(\s*([^\)]+)\s*\)", r"\1.IntValue", code)
		code = re.sub(r"GetConVarName\s*\(\s*([^\,]+)\s*,\s*", r"\1.GetName(", code)
		code = re.sub(r"GetConVarString\s*\(\s*([^\,]+)\s*,\s*", r"\1.GetString(", code)
		code = re.sub(r"HookConVarChange\s*\(\s*([^\,]+)\s*,\s*", r"\1.AddChangeHook(", code)
		code = re.sub(r"ResetConVar\s*\(\s*([^\,]+)\s*,\s*", r"\1.RestoreDefault(", code)
		code = re.sub(r"SendConVarValue\s*\(\s*([^\,]+)\s*,\s*", r"\1.ReplicateToClient(", code)

		# Only use the method if the original call has more than 2 parameters.
		code = re.sub(r"SetConVarBool\s*\(\s*([^\,]+)\s*,\s*([^\,]+)\s*,", r"\1.SetBool(\2,", code)
		code = re.sub(r"SetConVarBool\s*\(\s*([^\,]+)\s*,\s*([^\)]+)\s*\)", r"\1.BoolValue = \2", code)

		code = re.sub(r"SetConVarBounds\s*\(\s*([^\,]+)\s*,\s*", r"\1.SetBounds(", code)
		code = re.sub(r"SetConVarFlags\s*\(\s*([^\,]+)\s*,\s*([^\)]+)\s*\)", r"\1.Flags = \2", code)

		code = re.sub(r"SetConVarFloat\s*\(\s*([^\,]+)\s*,\s*([^\,]+)\s*,", r"\1.SetFloat(\2,", code)
		code = re.sub(r"SetConVarFloat\s*\(\s*([^\,]+)\s*,\s*([^\)]+)\s*\)", r"\1.FloatValue = \2", code)
		code = re.sub(r"SetConVarInt\s*\(\s*([^\,]+)\s*,\s*([^\,]+)\s*,", r"\1.SetInt(\2,", code)
		code = re.sub(r"SetConVarInt\s*\(\s*([^\,]+)\s*,\s*([^\)]+)\s*\)", r"\1.IntValue = \2", code)
		code = re.sub(r"SetConVarString\s*\(\s*([^\,]+)\s*,\s*", r"\1.SetString(", code)
		code = re.sub(r"UnhookConVarChange\s*\(\s*([^\,]+)\s*,\s*", r"\1.RemoveChangeHook(", code)

		# DataPack
		code = re.sub(r"CreateDataPack\s*\(\s*\)", r"new DataPack()", code)
		code = re.sub(r"WritePackCell\s*\(\s*([^\,]+)\s*,\s*", r"\1.WriteCell(", code)
		code = re.sub(r"WritePackFloat\s*\(\s*([^\,]+)\s*,\s*", r"\1.WriteFloat(", code)
		code = re.sub(r"WritePackString\s*\(\s*([^\,]+)\s*,\s*", r"\1.WriteString(", code)
		code = re.sub(r"WritePackFunction\s*\(\s*([^\,]+)\s*,\s*", r"\1.WriteFunction(", code)
		code = re.sub(r"ReadPackCell\s*\(\s*([^\)]+)\s*\)", r"\1.ReadCell()", code)
		code = re.sub(r"ReadPackFloat\s*\(\s*([^\)]+)\s*\)", r"\1.ReadFloat()", code)
		code = re.sub(r"ReadPackString\s*\(\s*([^\,]+)\s*,\s*", r"\1.ReadString(", code)
		code = re.sub(r"ReadPackFunction\s*\(\s*([^\)]+)\s*\)", r"\1.ReadFunction()", code)
		code = re.sub(r"ResetPack\s*\(\s*([^\,\)]+)\s*,?\s*([^\)]*)\s*\)", r"\1.Reset(\2)", code)
		code = re.sub(r"GetPackPosition\s*\(\s*([^\)]+)\s*\)", r"\1.Position", code)
		code = re.sub(r"SetPackPosition\s*\(\s*([^\,]+)\s*,\s*([^\)]+)\s*\)", r"\1.Position = \2", code)
		code = re.sub(r"IsStackEmptyckReadable\s*\(\s*([^\,]+)\s*,\s*", r"\1.IsReadable(", code)

		# DBDriver
		code = re.sub(r"SQL_GetDriver\s*\(", r"DBDriver.Find(", code)
		code = re.sub(r"SQL_GetDriverProduct\s*\(\s*([^\,]+)\s*,\s*", r"\1.GetProduct(", code)
		code = re.sub(r"SQL_GetDriverIdent\s*\(\s*([^\,]+)\s*,\s*", r"\1.GetIdentifier(", code)

		# DBResultSet
		code = re.sub(r"SQL_FetchMoreResults\s*\(\s*([^\)]+)\s*\)", r"\1.FetchMoreResults()", code)
		code = re.sub(r"SQL_HasResultSet\s*\(\s*([^\)]+)\s*\)", r"\1.HasResults", code)
		code = re.sub(r"SQL_GetRowCount\s*\(\s*([^\)]+)\s*\)", r"\1.RowCount", code)
		code = re.sub(r"SQL_GetFieldCount\s*\(\s*([^\)]+)\s*\)", r"\1.FieldCount", code)
		code = re.sub(r"SQL_GetAffectedRows\s*\(\s*([^\)]+)\s*\)", r"\1.AffectedRows", code)
		code = re.sub(r"SQL_GetInsertId\s*\(\s*([^\)]+)\s*\)", r"\1.InsertId", code)
		code = re.sub(r"SQL_FieldNumToName\s*\(\s*([^\,]+)\s*,\s*", r"\1.FieldNumToName(", code)
		code = re.sub(r"SQL_FieldNameToNum\s*\(\s*([^\,]+)\s*,\s*", r"\1.FieldNameToNum(", code)
		code = re.sub(r"SQL_FetchRow\s*\(\s*([^\)]+)\s*\)", r"\1.FetchRow()", code)
		code = re.sub(r"SQL_MoreRows\s*\(\s*([^\)]+)\s*\)", r"\1.MoreRows", code)
		code = re.sub(r"SQL_Rewind\s*\(\s*([^\)]+)\s*\)", r"\1.Rewind()", code)
		code = re.sub(r"SQL_FetchString\s*\(\s*([^\,]+)\s*,\s*", r"\1.FetchString(", code)
		code = re.sub(r"SQL_FetchFloats*\(\s*([^\,]+)\s*,\s*", r"\1.FetchFloat(", code)
		code = re.sub(r"SQL_FetchInt*\(\s*([^\,]+)\s*,\s*", r"\1.FetchInt(", code)
		code = re.sub(r"SQL_IsFieldNull*\(\s*([^\,]+)\s*,\s*", r"\1.IsFieldNull(", code)
		code = re.sub(r"SQL_FetchSize*\(\s*([^\,]+)\s*,\s*", r"\1.FetchSize(", code)

		# Transaction
		code = re.sub(r"SQL_CreateTransaction\s*\(\s*\)", r"new Transaction()", code)
		code = re.sub(r"SQL_AddQuery\s*\(\s*([^\,]+)\s*,\s*", r"\1.AddQuery(", code)

		# DBStatement
		code = re.sub(r"SQL_BindParamInt\s*\(\s*([^\,]+)\s*,\s*", r"\1.BindInt(", code)
		code = re.sub(r"SQL_BindParamFloat\s*\(\s*([^\,]+)\s*,\s*", r"\1.BindFloat(", code)
		code = re.sub(r"SQL_BindParamString\s*\(\s*([^\,]+)\s*,\s*", r"\1.BindString(", code)

		# Database
		code = re.sub(r"SQL_TConnect\s*\(", r"Database.Connect(", code)
		# Only replace if the optional ident argument isn't used.
		code = re.sub(r"SQL_ReadDriver\s*\(\s*([^\)\,]+)\s*\)", r"\1.Driver", code)
		code = re.sub(r"SQL_SetCharset\s*\(\s*([^\,]+)\s*,\s*", r"\1.SetCharset(", code)
		code = re.sub(r"SQL_EscapeString\s*\(\s*([^\,]+)\s*,\s*", r"\1.Escape(", code)
		code = re.sub(r"SQL_FormatQuery\s*\(\s*([^\,]+)\s*,\s*", r"\1.Format(", code)
		code = re.sub(r"SQL_IsSameConnection\s*\(\s*([^\,]+)\s*,\s*", r"\1.IsSameConnection(", code)
		code = re.sub(r"SQL_TQuery\s*\(\s*([^\,]+)\s*,\s*", r"\1.Query(", code)
		code = re.sub(r"SQL_ExecuteTransaction\s*\(\s*([^\,]+)\s*,\s*", r"\1.Execute(", code)

		# Event
		code = re.sub(r"FireEvent\s*\(\s*([^\,\)]+)\s*,?\s*([^\)]*)\s*\)", r"\1.Fire(\2)", code)
		code = re.sub(r"CancelCreatedEvent\s*\(\s*([^\)]+)\s*\)", r"\1.Cancel()", code)
		code = re.sub(r"GetEventBool\s*\(\s*([^\,]+)\s*,\s*", r"\1.GetBool(", code)
		code = re.sub(r"SetEventBool\s*\(\s*([^\,]+)\s*,\s*", r"\1.SetBool(", code)
		code = re.sub(r"GetEventInt\s*\(\s*([^\,]+)\s*,\s*", r"\1.GetInt(", code)
		code = re.sub(r"SetEventInt\s*\(\s*([^\,]+)\s*,\s*", r"\1.SetInt(", code)
		code = re.sub(r"GetEventFloat\s*\(\s*([^\,]+)\s*,\s*", r"\1.GetFloat(", code)
		code = re.sub(r"SetEventFloat\s*\(\s*([^\,]+)\s*,\s*", r"\1.SetFloat(", code)
		code = re.sub(r"GetEventString\s*\(\s*([^\,]+)\s*,\s*", r"\1.GetString(", code)
		code = re.sub(r"SetEventString\s*\(\s*([^\,]+)\s*,\s*", r"\1.SetString(", code)
		code = re.sub(r"GetEventName\s*\(\s*([^\,]+)\s*,\s*", r"\1.GetName(", code)
		code = re.sub(r"SetEventBroadcast\s*\(\s*([^\,]+)\s*,\s*([^\)]+)\s*\)", r"\1.BroadcastDisabled = \2", code)

		# DirectoryListing
		code = re.sub(r"ReadDirEntry\s*\(\s*([^\,]+)\s*,\s*", r"\1.GetNext(", code)

		# File
		code = re.sub(r"IsEndOfFile\s*\(\s*([^\)]+)\s*\)", r"\1.EndOfFile()", code)
		code = re.sub(r"ReadFile\s*\(\s*([^\,]+)\s*,\s*", r"\1.Read(", code)
		code = re.sub(r"ReadFileLine\s*\(\s*([^\,]+)\s*,\s*", r"\1.ReadLine(", code)
		code = re.sub(r"ReadFileString\s*\(\s*([^\,]+)\s*,\s*", r"\1.ReadString(", code)
		code = re.sub(r"FileSeek\s*\(\s*([^\,]+)\s*,\s*", r"\1.Seek(", code)
		code = re.sub(r"WriteFile\s*\(\s*([^\,]+)\s*,\s*", r"\1.Write(", code)
		code = re.sub(r"WriteFileLine\s*\(\s*([^\,]+)\s*,\s*", r"\1.WriteLine(", code)
		code = re.sub(r"WriteStringLine\s*\(\s*([^\,]+)\s*,\s*", r"\1.WriteString(", code)
		code = re.sub(r"FilePosition\s*\(\s*([^\)]+)\s*\)", r"\1.Position", code)
		# TODO: ReadFileCell & ReadIntX

		# Handles
		code = re.sub(r"CloseHandle\s*\(\s*([^\)]+)\s*\)", r"delete \1", code)

		# KeyValues
		code = re.sub(r"CreateKeyValues\s*\(\s*([^\)]+)\s*\)", r"new KeyValues(\1)", code)
		code = re.sub(r"KvSetString\s*\(\s*([^\,]+)\s*,\s*", r"\1.SetString(", code)
		code = re.sub(r"KvSetNum\s*\(\s*([^\,]+)\s*,\s*", r"\1.SetNum(", code)
		code = re.sub(r"KvSetUInt64\s*\(\s*([^\,]+)\s*,\s*", r"\1.SetUInt64(", code)
		code = re.sub(r"KvSetFloat\s*\(\s*([^\,]+)\s*,\s*", r"\1.SetFloat(", code)
		code = re.sub(r"KvSetColor\s*\(\s*([^\,]+)\s*,\s*", r"\1.SetColor(", code)
		code = re.sub(r"KvSetVector\s*\(\s*([^\,]+)\s*,\s*", r"\1.SetVector(", code)
		code = re.sub(r"KvGetString\s*\(\s*([^\,]+)\s*,\s*", r"\1.GetString(", code)
		code = re.sub(r"KvGetNum\s*\(\s*([^\,]+)\s*,\s*", r"\1.GetNum(", code)
		code = re.sub(r"KvGetFloat\s*\(\s*([^\,]+)\s*,\s*", r"\1.GetFloat(", code)
		code = re.sub(r"KvGetColor\s*\(\s*([^\,]+)\s*,\s*", r"\1.GetColor(", code)
		code = re.sub(r"KvGetUInt64\s*\(\s*([^\,]+)\s*,\s*", r"\1.GetUInt64(", code)
		code = re.sub(r"KvGetVector\s*\(\s*([^\,]+)\s*,\s*", r"\1.GetVector(", code)
		code = re.sub(r"KvJumpToKey\s*\(\s*([^\,]+)\s*,\s*", r"\1.JumpToKey(", code)
		code = re.sub(r"KvJumpToKeySymbol\s*\(\s*([^\,]+)\s*,\s*", r"\1.JumpToKeySymbol(", code)
		code = re.sub(r"KvGotoFirstSubKey\s*\(\s*([^\,\)]+)\s*,?\s*([^\)]*)\s*\)", r"\1.GotoFirstSubKey(\2)", code)
		code = re.sub(r"KvGotoNextKey\s*\(\s*([^\,\)]+)\s*,?\s*([^\)]*)\s*\)", r"\1.GotoNextKey(\2)", code)
		code = re.sub(r"KvSavePosition\s*\(\s*([^\)]+)\s*\)", r"\1.SavePosition()", code)
		code = re.sub(r"KvDeleteKey\s*\(\s*([^\,]+)\s*,\s*", r"\1.DeleteKey(", code)
		code = re.sub(r"KvDeleteThis\s*\(\s*([^\)]+)\s*\)", r"\1.DeleteThis()", code)
		code = re.sub(r"KvGoBack\s*\(\s*([^\)]+)\s*\)", r"\1.GoBack()", code)
		code = re.sub(r"KvRewind\s*\(\s*([^\)]+)\s*\)", r"\1.Rewind()", code)
		code = re.sub(r"KvGetSectionName\s*\(\s*([^\,]+)\s*,\s*", r"\1.GetSectionName(", code)
		code = re.sub(r"KvSetSectionName\s*\(\s*([^\,]+)\s*,\s*", r"\1.SetSectionName(", code)
		code = re.sub(r"KvGetDataType\s*\(\s*([^\,]+)\s*,\s*", r"\1.GetDataType(", code)
		code = re.sub(r"KeyValuesToFile\s*\(\s*([^\,]+)\s*,\s*", r"\1.ExportToFile(", code)
		code = re.sub(r"FileToKeyValues\s*\(\s*([^\,]+)\s*,\s*", r"\1.ImportFromFile(", code)
		code = re.sub(r"StringToKeyValues\s*\(\s*([^\,]+)\s*,\s*", r"\1.ImportFromString(", code)
		code = re.sub(r"KvSetEscapeSequences\s*\(\s*([^\,]+)\s*,\s*", r"\1.SetEscapeSequences(", code)
		code = re.sub(r"KvNodesInStack\s*\(\s*([^\)]+)\s*\)", r"\1.NodesInStack()", code)
		code = re.sub(r"KvCopySubkeys\s*\(\s*([^\,]+)\s*,\s*", r"\1.Import(", code)
		code = re.sub(r"KvFindKeyById\s*\(\s*([^\,]+)\s*,\s*", r"\1.FindKeyById(", code)
		code = re.sub(r"KvGetNameSymbol\s*\(\s*([^\,]+)\s*,\s*", r"\1.GetNameSymbol(", code)
		code = re.sub(r"KvGetSectionSymbol\s*\(\s*([^\,]+)\s*,\s*", r"\1.GetSectionSymbol(", code)
		
		# Menu
		code = re.sub(r"CreateMenu\s*\(\s*([^\)]+)\s*\)", r"new Menu(\1)", code)
		code = re.sub(r"DisplayMenu\s*\(\s*([^\,]+)\s*,\s*", r"\1.Display(", code)
		code = re.sub(r"DisplayMenuAtItem\s*\(\s*([^\,]+)\s*,\s*", r"\1.DisplayAt(", code)
		code = re.sub(r"AddMenuItem\s*\(\s*([^\,]+)\s*,\s*", r"\1.AddItem(", code)
		code = re.sub(r"InsertMenuItem\s*\(\s*([^\,]+)\s*,\s*", r"\1.InsertItem(", code)
		code = re.sub(r"RemoveMenuItem\s*\(\s*([^\,]+)\s*,\s*", r"\1.RemoveItem(", code)
		code = re.sub(r"RemoveAllMenuItems\s*\(\s*([^\)]+)\s*\)", r"\1.RemoveAllItems()", code)
		code = re.sub(r"GetMenuItem\s*\(\s*([^\,]+)\s*,\s*", r"\1.GetItem(", code)
		code = re.sub(r"GetMenuSelectionPosition\s*\(\s*([^\)]+)\s*\)", r"\1.Selection", code)
		code = re.sub(r"GetMenuItemCount\s*\(\s*([^\)]+)\s*\)", r"\1.ItemCount", code)
		code = re.sub(r"SetMenuPagination\s*\(\s*([^\,]+)\s*,\s*([^\)]+)\s*\)", r"\1.Pagination = \2", code)
		code = re.sub(r"GetMenuPagination\s*\(\s*([^\)]+)\s*\)", r"\1.Pagination", code)
		code = re.sub(r"GetMenuStyle\s*\(\s*([^\)]+)\s*\)", r"\1.Style", code)
		code = re.sub(r"SetMenuTitle\s*\(\s*([^\,]+)\s*,\s*", r"\1.SetTitle(", code)
		code = re.sub(r"GetMenuTitle\s*\(\s*([^\,]+)\s*,\s*", r"\1.GetTitle(", code)
		code = re.sub(r"CreatePanelFromMenu\s*\(\s*([^\)]+)\s*\)", r"\1.ToPanel()", code)
		code = re.sub(r"GetMenuExitButton\s*\(\s*([^\)]+)\s*\)", r"\1.ExitButton", code)
		code = re.sub(r"SetMenuExitButton\s*\(\s*([^\,]+)\s*,\s*([^\)]+)\s*\)", r"\1.ExitButton = \2", code)
		code = re.sub(r"GetMenuExitBackButton\s*\(\s*([^\)]+)\s*\)", r"\1.ExitBackButton", code)
		code = re.sub(r"SetMenuExitBackButton\s*\(\s*([^\,]+)\s*,\s*([^\)]+)\s*\)", r"\1.ExitBackButton = \2", code)
		code = re.sub(r"SetMenuNoVoteButton\s*\(\s*([^\,]+)\s*,\s*([^\)]+)\s*\)", r"\1.NoVoteButton = \2", code)
		code = re.sub(r"CancelMenu\s*\(\s*([^\)]+)\s*\)", r"\1.Cancel()", code)
		code = re.sub(r"GetMenuOptionFlags\s*\(\s*([^\)]+)\s*\)", r"\1.OptionFlags", code)
		code = re.sub(r"SetMenuOptionFlags\s*\(\s*([^\,]+)\s*,\s*([^\)]+)\s*\)", r"\1.OptionFlags = \2", code)
		code = re.sub(r"VoteMenu\s*\(\s*([^\,]+)\s*,\s*", r"\1.DisplayVote(", code)
		code = re.sub(r"VoteMenuToAll\s*\(\s*([^\,]+)\s*,\s*", r"\1.DisplayVoteToAll(", code)
		code = re.sub(r"SetVoteResultCallback\s*\(\s*([^\,]+)\s*,\s*([^\)]+)\s*\)", r"\1.VoteResultCallback = \2", code)

		# Panel
		code = re.sub(r"CreatePanel\s*\(\s*([^\)]*)\s*\)", r"new Panel(\1)", code)
		code = re.sub(r"GetPanelStyle\s*\(\s*([^\)]+)\s*\)", r"\1.Style", code)
		code = re.sub(r"SetPanelTitle\s*\(\s*([^\,]+)\s*,\s*", r"\1.SetTitle(", code)
		code = re.sub(r"DrawPanelItem\s*\(\s*([^\,]+)\s*,\s*", r"\1.DrawItem(", code)
		code = re.sub(r"DrawPanelText\s*\(\s*([^\,]+)\s*,\s*", r"\1.DrawText(", code)
		code = re.sub(r"CanPanelDrawFlags\s*\(\s*([^\,]+)\s*,\s*", r"\1.CanDrawFlags(", code)
		code = re.sub(r"SetPanelKeys\s*\(\s*([^\,]+)\s*,\s*", r"\1.SetKeys(", code)
		code = re.sub(r"SendPanelToClient\s*\(\s*([^\,]+)\s*,\s*", r"\1.Send(", code)
		code = re.sub(r"GetPanelTextRemaining\s*\(\s*([^\)]+)\s*\)", r"\1.TextRemaining", code)
		code = re.sub(r"GetPanelCurrentKey\s*\(\s*([^\)]+)\s*\)", r"\1.CurrentKey", code)
		code = re.sub(r"SetPanelCurrentKey\s*\(\s*([^\,]+)\s*,\s*([^\)]+)\s*\)", r"\1.CurrentKey = \2", code)

		# TODO: Protobuf

		# Regex
		code = re.sub(r"CompileRegex\s*\(\s*([^\)]*)\s*\)", r"new Regex(\1)", code)
		code = re.sub(r"MatchRegex\s*\(\s*([^\,]+)\s*,\s*", r"\1.Match(", code)
		code = re.sub(r"GetRegexSubString\s*\(\s*([^\,]+)\s*,\s*", r"\1.GetSubString(", code)

		# SMCParser
		code = re.sub(r"SMC_CreateParser\s*\(\s*\)", r"new SMCParser()", code)
		code = re.sub(r"SMC_ParseFile\s*\(\s*([^\,]+)\s*,\s*", r"\1.ParseFile(", code)
		code = re.sub(r"SMC_SetParseStart\s*\(\s*([^\,]+)\s*,\s*([^\)]+)\s*\)", r"\1.OnStart = \2", code)
		code = re.sub(r"SMC_SetParseEnd\s*\(\s*([^\,]+)\s*,\s*([^\)]+)\s*\)", r"\1.OnEnd = \2", code)
		# TODO: Split up into 3 seperate lines?
		#code = re.sub(r"SMC_SetReaders\s*\(\s*([^\,]+)\s*,\s*([^\)]+)\s*\)", r"\1.OnEnterSection = \2", code)
		#code = re.sub(r"SetPanelCurrentKey\s*\(\s*([^\,]+)\s*,\s*([^\)]+)\s*\)", r"\1.OnLeaveSection = \2", code)
		#code = re.sub(r"SetPanelCurrentKey\s*\(\s*([^\,]+)\s*,\s*([^\)]+)\s*\)", r"\1.OnKeyValue = \2", code)
		code = re.sub(r"SMC_SetRawLine\s*\(\s*([^\,]+)\s*,\s*([^\)]+)\s*\)", r"\1.OnRawLine = \2", code)
		code = re.sub(r"SMC_GetErrorString\s*\(\s*([^\,]+)\s*,\s*", r"\1.GetErrorString(", code)

		# TopMenu
		code = re.sub(r"CreateTopMenu\s*\(\s*([^\)]*)\s*\)", r"new TopMenu(\1)", code)
		code = re.sub(r"LoadTopMenuConfig\s*\(\s*([^\,]+)\s*,\s*", r"\1.LoadConfig(", code)
		code = re.sub(r"AddToTopMenu\s*\(\s*([^\,]+)\s*,\s*([^\,]+)\s*,\s*TopMenuObject_Category", r"\1.AddCategory(\2, ", code)
		code = re.sub(r"AddToTopMenu\s*\(\s*([^\,]+)\s*,\s*([^\,]+)\s*,\s*TopMenuObject_Item", r"\1.AddItem(\2, ", code)
		code = re.sub(r"GetTopMenuInfoString\s*\(\s*([^\,]+)\s*,\s*", r"\1.GetInfoString(", code)
		code = re.sub(r"GetTopMenuObjName\s*\(\s*([^\,]+)\s*,\s*", r"\1.GetObjName(", code)
		code = re.sub(r"RemoveFromTopMenu\s*\(\s*([^\,]+)\s*,\s*", r"\1.Remove(", code)
		code = re.sub(r"DisplayTopMenu\s*\(\s*([^\,]+)\s*,\s*", r"\1.Display(", code)
		code = re.sub(r"DisplayTopMenuCategory\s*\(\s*([^\,]+)\s*,\s*", r"\1.DisplayCategory(", code)
		code = re.sub(r"FindTopMenuCategory\s*\(\s*([^\,]+)\s*,\s*", r"\1.FindCategory(", code)
		code = re.sub(r"SetTopMenuTitleCaching\s*\(\s*([^\,]+)\s*,\s*([^\)]+)\s*\)", r"\1.CacheTitles = \2", code)

		# _: int retagging
		#code = re.sub(r"_:([a-zA-Z0-9_]+(\[[a-zA-Z0-9_]+\])*)", r"view_as<int>(\1)", code)

	with open(sys.argv[i] + '.m', 'w') as f:
		f.write(code)