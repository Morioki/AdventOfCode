module Day1

open System
open Helpers

let wordToDigit = 
    [ "one", "1";
      "two", "2";
      "three", "3";
      "four", "4";
      "five","5";
      "six","6";
      "seven","7";
      "eight","8";
      "nine","9"] |> Map.ofList

let replaceString (replaceMap: Map<string, string>) (input: string) : string =
    let mutable result = new System.Text.StringBuilder(input.Length)
    let mutable i = 0
    for i in 0 .. input.Length-1 do
    // while i < input.Length do
        let foundKeyOpt =
            replaceMap
            |> Map.tryFindKey (fun key _ -> 
                if (i + key.Length <= input.Length && input.Substring(i, key.Length) = key) then
                    true // Some(key)
                else 
                    false //None
            )
        
        let foundKey = 
            match foundKeyOpt with 
                | Some x -> x
                | None -> ""
        
        let foundVal = 
            replaceMap
            |> Map.tryFind foundKey 

        match foundVal with 
        | Some x -> 
            result.Append(x) |> ignore
            // i <- i <- i + 1
        | None -> 
            result.Append(input.[i]) |> ignore
            // i <- i + 1

    result |> string

let task1_extractCalibration (line: string): int =
    let fstDigit = 
        try 
            line |> Seq.find Char.IsDigit 
        with
        | :? System.Collections.Generic.KeyNotFoundException -> '0'

    let sndDigit = 
        try 
            line |> Seq.findBack Char.IsDigit 
        with
        | :? System.Collections.Generic.KeyNotFoundException -> '0'

    String [| fstDigit;sndDigit |] |> int

let task2_extract (line: string): int = 
    let newString = 
        line 
        |> replaceString wordToDigit
   
    // line |> Console.WriteLine
    // newString |> Console.WriteLine
    newString |> task1_extractCalibration

let task1 (data:seq<string>): int =
    data |> Seq.sumBy task1_extractCalibration

let task2 (data:seq<string>): int =
    // data |> Seq.head |> task2_extract
    data |> Seq.sumBy task2_extract

let runTasks (data:seq<string>): unit =
    try 
        printfn $"Task 1: {(data |> task1)}"
        printfn $"Task 2: {(data |> task2)}"
    with 
    | :? System.NotImplementedException -> printfn ""
    | :? System.Collections.Generic.KeyNotFoundException -> printfn ""
    
    