open System

open Helpers

[<EntryPoint>]
let main args =
       
    // First Arg = TestFlag
    let testFlag = args[0] |> int
    // Second Arg = Day
    let dayVal = 
        match Array.length(args) with
        | 0 -> "1"
        | 1 -> "1"
        | _ -> args[1]
        |> int

    // pullDataset dayVal testFlag |> Seq.iter System.Console.WriteLine
    match dayVal with
    | 1 -> pullDataset dayVal testFlag |> Day1.runTasks
    | 2 -> pullDataset dayVal testFlag |> Day2.runTasks
    
    | _ -> invalidArg (nameof dayVal) (sprintf "Day %d is not a valid parameter" dayVal)
    |> ignore

    0 // return an integer exit code