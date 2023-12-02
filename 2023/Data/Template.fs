let task1 (data:seq<string>): int =
    nyi

let task2 (data:seq<string>): int =
    nyi

let runTasks (data:seq<string>): unit =
    try 
        printfn $"Task 1: {(data |> task1)}"
        printfn $"Task 2: {(data |> task2)}"
    with 
    | :? System.NotImplementedException -> printfn ""
    | :? System.Collections.Generic.KeyNotFoundException -> printfn ""
    
    
