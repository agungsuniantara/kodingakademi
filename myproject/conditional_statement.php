<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <?php
        $age = 20;

        if ($age >= 18) {
            echo "You are an adult.";
        }

        $age = 16;

        if ($age >= 18) {
            echo "You are an adult.";
        } else {
            echo "You are a minor.";
        }

        $score = 85;

        if ($score >= 90) {
            echo "Grade: A";
        } elseif ($score >= 80) {
            echo "Grade: B";
        } elseif ($score >= 70) {
            echo "Grade: C";
        } else {
            echo "Grade: D";
        }

        $day = "Wednesday";

        switch ($day) {
            case "Monday":
                echo "Start of the work week.";
                break;
            case "Friday":
                echo "End of the work week.";
                break;
            case "Saturday":
            case "Sunday":
                echo "It's the weekend!";
                break;
            default:
                echo "Middle of the work week.";
        }

        $is_logged_in = true;
        $message = $is_logged_in ? "Welcome back!" : "Please log in.";
        echo $message;

        $count = 1;

        while ($count <= 5) {
            echo "Count: $count <br>";
            $count++;
        }

        $count = 1;

        do {
            echo "Count: $count <br>";
            $count++;
        } while ($count <= 5);

        for ($i = 1; $i <= 5; $i++) {
            echo "Iteration: $i <br>";
        }

        $colors = ["Red", "Green", "Blue", "Yellow"];

        foreach ($colors as $color) {
            echo "Color: $color <br>";
        }

        for ($i = 1; $i <= 3; $i++) {
            echo "Outer Loop Iteration: $i <br>";
            for ($j = 1; $j <= 2; $j++) {
                echo "Inner Loop Iteration: $j <br>";
            }
        }
    ?>
</body>
</html>