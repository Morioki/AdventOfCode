module day1

open System.Text.Json

let getJson value =
    let json = JsonSerializer.Serialize(value)
    value, json