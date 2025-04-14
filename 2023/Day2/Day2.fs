module Day2

open System
open Helpers

let redLimit = 12
let greenLimit = 13
let blueLimit = 14

type DataSample = {
    Red: int
    Green: int
    Blue: int
}

type Game = {
    GameID: int
    Samples: DataSample list
}

let splitToTuple (str: string) =
    let splitStr = str.Split(" ")
    (splitStr[0],splitStr[1])

let setRed (a: DataSample) (count: int): DataSample =
    {a with Red = count}

let setGreen (a: DataSample) (count: int): DataSample =
    {a with Green = count}

let setBlue (a: DataSample) (count: int): DataSample =
    {a with Blue = count}

let printSample (s:DataSample) =
    printfn $"Red: {s.Red}, Blue: {s.Blue}, Green: {s.Green}"

let extractGameID (game: string): int = 
    let Id = game.Split(" ")[1]
    Id.Trim() |> int

let buildSample (str: string): DataSample =
    let tmp = str.Split(",")
    let el = Array.map (fun (s:string) -> splitToTuple (s.Trim()) ) tmp

    let mutable sample = {Red = 0; Green = 0; Blue = 0}

    for i in 0 .. el.Length - 1 do
        match el[i] with
        | (a,b) when b = "red" -> sample <- (setRed sample (a |> int))
        | (a,b) when b = "blue" -> sample <- (setBlue sample (a |> int))
        | (a,b) when b = "green" -> sample <- (setGreen sample (a |> int))
        | _ -> ()

    sample

let splitSamples (line: string) =
    let tmp = line.Split(";")
    let pulls = Array.map (fun (samp:string) -> samp.Trim()) tmp

    pulls |> Array.map buildSample |> Array.toList

let parseLine (line: string): Game =
    let GameId = line.Split(":").[0].Trim() |> extractGameID
    let samples = line.Split(":").[1].Trim() |> splitSamples
    
    {GameID = GameId; Samples=samples}

let validRow (sample: DataSample): bool =
    match sample with
    | x when x.Red > redLimit -> false
    | x when x.Blue > blueLimit -> false
    | x when x.Green > greenLimit -> false 
    | _ -> true

let checkGame (game:Game): int = 
    let Id = game.GameID
    let samples = game.Samples

    if List.forall validRow samples then
        Id
    else 
        0    

let minRed (game: Game): int =
    (game.Samples |> List.maxBy (fun x -> x.Red )).Red

let minGreen (game: Game): int =
    (game.Samples |> List.maxBy (fun x -> x.Green )).Green

let minBlue (game: Game): int =
    (game.Samples |> List.maxBy (fun x -> x.Blue )).Blue

let calculatePower (game: Game) =
    (minRed game) * (minGreen game) * (minBlue game)

let task1 (data:seq<string>): int =
    data |> Seq.map parseLine |> Seq.sumBy checkGame

let task2 (data:seq<string>): int =
    data |> Seq.map parseLine |> Seq.sumBy calculatePower

let runTasks (data:seq<string>): unit =
    try 
        printfn $"Task 1: {(data |> task1)}"
        printfn $"Task 2: {(data |> task2)}"
    with 
    | :? System.NotImplementedException -> printfn ""
    | :? System.Collections.Generic.KeyNotFoundException -> printfn ""
    
    
