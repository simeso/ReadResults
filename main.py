import glob
import os

#/Volumes/Seagate/MASTER/ResultsFinal/
#/Volumes/SimenS/ResultsFinalWO/
def read_results_magnus():
    optimal_results = {}

    with open('Routes generation 50 with total time.txt', 'r') as reader:

        for line in reader:
            lineArr = line.split(",")
            key = lineArr[0].split("/")
            key2 = key[3]
            key3 = key2.split(".")[0]

            if lineArr[1] == " Not Solved":
                optimal_results[key3] = (float(lineArr[2]), float(lineArr[3]), False)
            else:
                optimal_results[key3] = (float(lineArr[2]), float(lineArr[3]), True)

    return optimal_results


def iterate_files():
    our_results = {}
    os.chdir("/Volumes/Seagate/MASTER/ResultsFinal/1D")
    for file in glob.glob("*.txt"):
        result = read_results(file)

        filename = file.split("r")[0]

        if our_results.__contains__(filename):
            our_results[filename].append(result)
        else:
            our_results[filename] = [result]

    os.chdir("/Volumes/Seagate/MASTER/ResultsFinal//2D")
    for file in glob.glob("*.txt"):
        result = read_results(file)

        filename = file.split("r")[0]

        if our_results.__contains__(filename):
            our_results[filename].append(result)
        else:
            our_results[filename] = [result]

    os.chdir("/Volumes/Seagate/MASTER/ResultsFinal/3D")
    for file in glob.glob("*.txt"):
        result = read_results(file)

        filename = file.split("r")[0]

        if our_results.__contains__(filename):
            our_results[filename].append(result)
        else:
            our_results[filename] = [result]

    return our_results

def read_results(filename):
    with open(filename, 'r') as reader:

        for line in reader:
            if "ObjectiveValue" in line:
                return float(line.split(":")[1])

def calculate_optimality_gap(result_magnus, result_us):
    optimality_gaps = {}
    min_gaps = {}
    max_gaps = {}
    for key, val in result_magnus.items():


        if not val[2] and val[0] == 9.99999999E8:
            # print("Ulik - Ulost:", key, val[0], val[1])
            continue

        if not result_us.__contains__(key):
            continue

        sum = 0
        count = 0

        max = 0
        min = 1000000
        for res in result_us[key]:
            sum += res
            count += 1
            if res > max:
                max = res
            if res < min:
                min = res

        if val[0] != val[1]:
            pass
            # print("Ulik: ", key, ":", val[0], val[1])

        avg = sum/count
        gap = (val[0] - avg)/val[0] * 100
        minGap = (val[0] - max)/val[0] * 100
        maxGap = (val[0] - min) / val[0] * 100

        # if gap < 0.001:
        #     gap = 0

        if gap > 2:
            # print(key, ":", gap, ":", minGap, ":", maxGap)
            # print(key)
            pass

        if gap < 0.0 or minGap < 0.0 or maxGap < 0.0:
            print(key, ":", gap, ":", minGap, ":", maxGap)
            # print(key, ":", gap)

        optimality_gaps[key] = gap
        min_gaps[key] = minGap
        max_gaps[key] = maxGap

    print(len(optimality_gaps))

    return optimality_gaps, min_gaps, max_gaps


def calculate_average_gap(optimality_gaps):
    average_gap_num_requests = {}
    for key, val in optimality_gaps.items():
        num_requests = key.split("R")[0].split("D")[1]

        if average_gap_num_requests.__contains__(num_requests):
            average_gap_num_requests[num_requests].append(val)
        else:
            average_gap_num_requests[num_requests] = [val]

    for key in average_gap_num_requests.keys():

        sum = 0
        count = 0

        for res in average_gap_num_requests[key]:
            sum += res
            count += 1

        print(key, ":", sum/count)


result_magnus = read_results_magnus()
result_us = iterate_files()
optimality_gaps, min_gaps, max_gaps = calculate_optimality_gap(result_magnus, result_us)
calculate_average_gap(optimality_gaps)
# calculate_average_gap(min_gaps)
# calculate_average_gap(max_gaps)
