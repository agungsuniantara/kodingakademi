<!DOCTYPE html>
<html>
    <body>
    <?php
    $shop = array( 
               array("ID"=>"E001","NAME"=>"William Smith", "EMAIL"=>"WilliamSmith@gmail.com" , "POSITION"=>"CEO", "PHONE"=>620828978),
               array("ID"=>"E001","NAME"=>"William Smith", "EMAIL"=>"WilliamSmith@gmail.com" , "POSITION"=>"CEO", "PHONE"=>620828978),
               array("ID"=>"E001","NAME"=>"William Smith", "EMAIL"=>"WilliamSmith@gmail.com" , "POSITION"=>"CEO", "PHONE"=>620828978),
               array("ID"=>"E001","NAME"=>"William Smith", "EMAIL"=>"WilliamSmith@gmail.com" , "POSITION"=>"CEO", "PHONE"=>620828978),
               array("ID"=>"E001","NAME"=>"William Smith", "EMAIL"=>"WilliamSmith@gmail.com" , "POSITION"=>"CEO", "PHONE"=>620828978), 
             );
    ?>
    <table border="1">
    <thead>
        <tr>
            <th><?php echo implode('<th>', array_keys(current($shop))); ?></th>
        </tr>
    </thead>
    <tbody>
    <?php foreach ($shop as $row): ?>
        <tr>
            <td><?php echo implode('<td>', $row); ?></td>
        </tr>
    <?php endforeach; ?>
    </tbody>
    </table>
    </body>
</html>