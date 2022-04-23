# CodeJam2021-round1B-digitBlocks
My solution of CodeJam 2021 roundB digit blocks

This solution only passes the first and will get a WA for the set 2. It can be improved with DP.

## My logic for this solution

For each tower I reserve the top 2 position for the 8s and 9s digits. So if I read 8 or 9, I insert it in the highest unfinished tower and if iI read a digit in range(8) I will insert it in the highest tower with less than B-2 blocks.

If there are no such tower, I insert the block anywhere

This solution is a simple greedy method and not guarantee to ger the best score but anyway you will have at least 90% of the max score possible. Whicj allows you to pass the test set 1.
