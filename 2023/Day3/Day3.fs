module Day3

open System
open System.Text.RegularExpressions
open Helpers

let extractPartNumbers (data:seq<string>) =
    let regex  = new Regex("\\d+")
    let captureNumbers (line:string): int seq = 
        regex.Matches(line) |> Seq.cast<Match> |> Seq.map (fun x -> int x.Value)

    data |> Seq.collect captureNumbers

let build2DArray (data:seq<string>) =
    Array2D.init (Seq.length data) (Seq.length (Seq.head data)) (fun i j -> (Seq.item i data).[j])

let printPartNumbers (data: string seq) =
    data |> Seq.iter Console.WriteLine

let printArray2D array =
    array |> Array2D.iteri (fun i j x -> printfn " [%d,%d] = %c" i j x)

let builddata (data:seq<string>) =
    let partNumbers = data |> extractPartNumbers
    let array = data |> build2DArray

    partNumbers, array

let findIndices (array: char array2d) (str: char) =
    let mutable indices = []
    for i in 0 .. (array |> Array2D.length1) - 1 do
        for j in 0 .. (array |> Array2D.length2) - 1 do
            if array.[i, j] = str then
                indices <- (i, j) :: indices
    indices |> List.rev

let checkAround array x y =
    let regex = new Regex("[^\\d+. a-zA-Z]")
    let rowLim, colLim = (array |> Array2D.length1), (array |> Array2D.length2)
    let indicies = [(-1, -1); (-1, 0); (-1, 1); (0, -1); (0, 1); (1, -1); (1, 0); (1, 1)]

    printfn $"Checking around ({x},{y})"

    indicies 
    |> List.map (fun (dx,dy) -> (x + dx, y + dy))
    |> List.filter (fun (i,j) -> i >= 0 && j >= 0 && i < rowLim && j < colLim)
    |> List.map (fun (i, j) -> array.[i,j])
    |> List.exists (fun (el: char) -> regex.IsMatch(Char.ToString(el)))
    |> Console.WriteLine

    nyi

let checkValid indices array =
    indices 
    |> List.exists (fun (i, j) -> checkAround array i j)

let task1 (data:seq<string>): int =
    let numbers, array = data |> builddata

    numbers 
    |> Seq.head
    |> Console.WriteLine

    // numbers
    // |> Seq.head
    // |> checkValid (findIndices array (char ))
    // // |> Seq.toList
    // // |> List.filter (fun (x: int) -> checkValid (findIndices array (char x)) array )
    // |> Console.WriteLine


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
    
    
// Plan
// Extract Numbers from Dataset
// Iterate through 2d array of dataset 