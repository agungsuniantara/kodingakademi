<!DOCTYPE html>
<html>
    <head></head>
    <body>
    <?php
    $shop = array( 
               array("title"=>"rose", "price"=>1.25 , "number"=>15),
               array("title"=>"daisy", "price"=>0.75 , "number"=>25),
               array("title"=>"orchid", "price"=>1.15 , "number"=>7) 
             );
    $ukuran = count($shop);
    ?>
    <table border="1">
        <?php for($i = 0; $i < $ukuran; $i++):?>
        <tr>
            <td><?php print_r($shop[$i]); ?></td>
        </tr>
        <?php endfor; ?>
    </table>
    </body>
</html>