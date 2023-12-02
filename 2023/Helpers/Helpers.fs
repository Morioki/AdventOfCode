module Helpers

open System
open System.IO


let nyi<'T> : 'T = raise (System.NotImplementedException())

let pullDataset (day : int) (testflag : int) =  
    let path = 
        match testflag with
        | 0 -> Path.Combine(@".", $"Data/day{day}/dataset.txt")
        | 1 -> Path.Combine(@".", $"Data/day{day}/dataset.test.txt")
        | _ -> raise (System.ArgumentException())

    printfn $"Loading Datafile: {path}"
    printfn ""
    
    path |> File.ReadAllLines |> seq

