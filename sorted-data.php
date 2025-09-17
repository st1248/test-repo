<?php
// Sample data array
$data = [
    ["Christopher Diaz", "458-02-6124", "5299-1561-5689-1938"],
    ["Rick Edwards", "612-20-6832", "5293-8502-0071-3058"],
    ["Victor Faulkner", "300-62-3266", "5548-0246-6336-5664"],
    ["Lisa Garrison", "660-03-8360", "4539-5385-7425-5825"],
    ["Marjorie Green", "213-46-8915", "4916-9766-5240-6147"],
    ["Mark Hall", "449-48-3135", "4556-0072-1294-7415"],
];

// Sort by name (first column)
usort($data, function($a, $b) {
    return strcmp($a[0], $b[0]);
});
?>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Sorted Data Table (PHP)</title>
    <style>
        body { font-family: Arial, sans-serif; background: #f4f4f4; margin: 0; padding: 0; }
        .container { max-width: 900px; margin: 40px auto; background: #fff; border-radius: 8px; box-shadow: 0 2px 8px rgba(0,0,0,0.1); padding: 32px; }
        h1 { text-align: center; color: #333; }
        table { width: 100%; border-collapse: collapse; margin-top: 32px; }
        th, td { padding: 12px 16px; border-bottom: 1px solid #ddd; text-align: left; }
        th { background: #e3e3e3; }
        tr:hover { background: #f1f1f1; }
    </style>
</head>
<body>
    <div class="container">
        <h1>Sorted Data Table (PHP)</h1>
        <table>
            <thead>
                <tr>
                    <th>Name</th>
                    <th>SSN</th>
                    <th>Card Number</th>
                </tr>
            </thead>
            <tbody>
                <?php foreach ($data as $row): ?>
                <tr>
                    <td><?= htmlspecialchars($row[0]) ?></td>
                    <td><?= htmlspecialchars($row[1]) ?></td>
                    <td><?= htmlspecialchars($row[2]) ?></td>
                </tr>
                <?php endforeach; ?>
            </tbody>
        </table>
    </div>
</body>
</html>
