@{
    IncludeRules = @('PS*')
    ExcludeRules = @('PSAvoidUsingWriteHost')
    Severity = @('Error', 'Warning', 'Information')
    Rules = @{
        PSAvoidLongLines = @{
            Enable            = $true
            MaximumLineLength = 79
        }
    }
}
