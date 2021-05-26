import glob
import os

#/Volumes/Seagate/MASTER/ResultsFinal/
#/Volumes/SimenS/ResultsFinalWO/
import time
import json

from Result_file import ResultFile


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

    # #For saving the dataframe
    # os.chdir("/Volumes/Seagate/MASTER/ResultsFinal/1D")
    # for file in glob.glob("*10-20Wr1.txt"):
    #     result = read_results(file)
    #
    #     filename = file.split("r")[0]
    #
    #     if our_results.__contains__(filename):
    #         our_results[filename].append(result.__dict__)
    #     else:
    #         our_results[filename] = [result.__dict__]

    os.chdir("/Volumes/Seagate/MASTER/ResultsFinal/1D")
    for file in glob.glob("*.txt"):
        result = read_results(file)

        filename = file.split("r")[0]

        if our_results.__contains__(filename):
            our_results[filename].append(result.__dict__)
        else:
            our_results[filename] = [result.__dict__]

    os.chdir("/Volumes/Seagate/MASTER/ResultsFinal//2D")
    for file in glob.glob("*.txt"):
        result = read_results(file)

        filename = file.split("r")[0]

        if our_results.__contains__(filename):
            our_results[filename].append(result.__dict__)
        else:
            our_results[filename] = [result.__dict__]

    os.chdir("/Volumes/Seagate/MASTER/ResultsFinal/3D")
    for file in glob.glob("*.txt"):
        result = read_results(file)

        filename = file.split("r")[0]

        if our_results.__contains__(filename):
            our_results[filename].append(result.__dict__)
        else:
            our_results[filename] = [result.__dict__]

    #Sjekk om dette funker
    # with open('/Volumes/Seagate/MASTER/our_results.txt', 'w') as outfile:
    #     json.dump(our_results, outfile)

    # print(our_results)
    return our_results

def read_saved_data(filename):
    with open(filename) as json_file:
        data = json.load(json_file)
    return data

def read_results(filename):
    result_file = ResultFile()
    with open(filename, 'r') as reader:
        for line in reader:

            # objective_value
            if "ObjectiveValue:" in line:
                ResultFile.set_objective_value(result_file, float(line.split(":")[1]))

            # routes
            if "Routes" in line:
                route_dict = {}
                temporary_string = (line.split(":")[1])
                temporary_string = (temporary_string.split("{")[1])
                temporary_string = (temporary_string.split("}")[0])
                temporary_list = temporary_string.split("=")
                for k in range(1, len(temporary_list)):
                    route_to_key = (temporary_list[k].split("[")[1])
                    route_to_key = (route_to_key.split("]")[0])
                    route_to_key = route_to_key.split(",")
                    route_to_key_final = []
                    for i in range(len(route_to_key)):
                        if route_to_key[i] != '':
                            route_to_key_final.append(int(route_to_key[i]))
                    route_dict[k] = route_to_key_final
                ResultFile.set_routes(result_file, route_dict)

            # unhandled
            if "Unhandled:" in line:
                temporary_string = (line.split(":")[1])
                temporary_string = (temporary_string.split("[")[1])
                temporary_string = (temporary_string.split("]")[0])
                temporary_list_0 = temporary_string.split(",")
                temporary_list = []
                for i in range(len(temporary_list_0)):
                    if temporary_list_0[i] != '':
                        temporary_list.append(int(temporary_list_0[i]))
                ResultFile.set_unhandled(result_file, temporary_list)

             # used_vehicles
            if "UsedVehicles:" in line:
                ResultFile.set_used_vehicles(result_file, float(line.split(":")[1]))

            # # optimality_gap # Her bør vi lese inn optimalitets gapet ifølge objektivverdi fra den andre filen osv
            # if "OptimalityGap" in line:
            #     ResultFile.set_optimality_gap(result_file, float(line.split(":")[1]))

            # preprocessing_time
            if "PreprocessingTime:" in line:
                ResultFile.set_preprocessing_time(result_file, float(line.split(":")[1]))

            # initial_value
            if "InitialValue:" in line:
                ResultFile.set_initial_value(result_file, float(line.split(":")[1]))

            # initial_solution_time
            if "InitialSolutionTime:" in line:
                ResultFile.set_initial_solution_time(result_file, float(line.split(":")[1]))

            # time_used_ALNS
            if "TimeUsedALNS:" in line:
                ResultFile.set_time_used_ALNS(result_file, float(line.split(":")[1]))

            # iterations_ALNS
            if "IterationsALNS:" in line:
                ResultFile.set_iterations_ALNS(result_file, float(line.split(":")[1]))

            # value_of_best_solution
            if "ValueOfBestSolution:" in line:
                temporary_string = (line.split(":")[1])
                temporary_string = (temporary_string.split("[")[1])
                temporary_string = (temporary_string.split("]")[0])
                temporary_list_0 = temporary_string.split(",")
                temporary_list = []
                for i in range(len(temporary_list_0)):
                    if temporary_list_0[i] != '':
                        temporary_list.append(float(temporary_list_0[i]))
                ResultFile.set_value_of_best_solution(result_file, temporary_list)

            # time_of_best_solution
            if "TimeOfBestSolution:" in line:
                temporary_string = (line.split(":")[1])
                temporary_string = (temporary_string.split("[")[1])
                temporary_string = (temporary_string.split("]")[0])
                temporary_list_0 = temporary_string.split(",")
                temporary_list = []
                for i in range(len(temporary_list_0)):
                    if temporary_list_0[i] != '':
                        temporary_list.append(float(temporary_list_0[i]))
                ResultFile.set_time_of_best_solution(result_file, temporary_list)

            # iterations_of_best_solution
            if "IterationsOfBestSolution:" in line:
                temporary_string = (line.split(":")[1])
                temporary_string = (temporary_string.split("[")[1])
                temporary_string = (temporary_string.split("]")[0])
                temporary_list_0 = temporary_string.split(",")
                temporary_list = []
                for i in range(len(temporary_list_0)):
                    if temporary_list_0[i] != '':
                        temporary_list.append(int(temporary_list_0[i]))
                ResultFile.set_iterations_of_best_solution(result_file, temporary_list)

            # removal_operator_of_best_solution
            if "RemovalOperatorOfBestSolution:" in line:
                temporary_string = (line.split(":")[1])
                temporary_string = (temporary_string.split("[")[1])
                temporary_string = (temporary_string.split("]")[0])
                temporary_list = temporary_string.split(",")
                ResultFile.set_removal_operator_of_best_solution(result_file, temporary_list)

            # insertion_operator_of_best_solution
            if "InsertionOperatorOfBestSolution:" in line:
                temporary_string = (line.split(":")[1])
                temporary_string = (temporary_string.split("[")[1])
                temporary_string = (temporary_string.split("]")[0])
                temporary_list = temporary_string.split(",")
                ResultFile.set_insertion_operator_of_best_solution(result_file, temporary_list)

            # scheduling_insertion_did_nothing
            if "SchedulingInsertionDidNothing:" in line:
                ResultFile.set_scheduling_insertion_did_nothing(result_file, float(line.split(":")[1]))

            # num_calls_scheduling
            if "NumCallsScheduling:" in line:
                ResultFile.set_num_calls_scheduling(result_file, float(line.split(":")[1]))

            # average_time_scheduling
            if "AverageTimeScheduling:" in line:
                ResultFile.set_average_time_scheduling(result_file, float(line.split(":")[1]))

            # num_feasibility_checks
            if "NumFeasibilityChecks:" in line:
                ResultFile.set_num_feasibility_checks(result_file, float(line.split(":")[1]))

            # num_previously_checked
            if "NumPreviouslyChecked:" in line:
                ResultFile.set_num_previously_checked(result_file, float(line.split(":")[1]))

            # percentage_previously_checked
            if "PercentagePreviouslyChecked:" in line:
                ResultFile.set_percentage_previously_checked(result_file, float(line.split(":")[1]))

            # average_removal_time
            if "AverageRemovalTime:" in line:
                ResultFile.set_average_removal_time(result_file, float(line.split(":")[1]))

            # removal_not_used
            if "RemovalNotUsed:" in line:
                ResultFile.set_removal_not_used(result_file, float(line.split(":")[1]))

            # removal_names
            if "RemovalNames:" in line:
                temporary_string = (line.split(":")[1])
                temporary_string = (temporary_string.split("[")[1])
                temporary_string = (temporary_string.split("]")[0])
                temporary_list = temporary_string.split(",")
                ResultFile.set_removal_names(result_file, temporary_list)

            # removal_usage
            if "RemovalUsage:" in line:
                temporary_string = (line.split(":")[1])
                temporary_string = (temporary_string.split("[")[1])
                temporary_string = (temporary_string.split("]")[0])
                temporary_list_0 = temporary_string.split(",")
                temporary_list = []
                for i in range(len(temporary_list_0)):
                    if temporary_list_0[i] != '':
                        temporary_list.append(int(temporary_list_0[i]))
                ResultFile.set_removal_usage(result_file, temporary_list)

            # removal_usage_total_time
            if "RemovalUsageTotalTime:" in line:
                temporary_string = (line.split(":")[1])
                temporary_string = (temporary_string.split("[")[1])
                temporary_string = (temporary_string.split("]")[0])
                temporary_list_0 = temporary_string.split(",")
                temporary_list = []
                for i in range(len(temporary_list_0)):
                    if temporary_list_0[i] != '':
                        temporary_list.append(float(temporary_list_0[i]))
                ResultFile.set_removal_usage_total_time(result_file, temporary_list)

            # removal_usage_average_time
            if "RemovalUsageAverageTime:" in line:
                temporary_string = (line.split(":")[1])
                temporary_string = (temporary_string.split("[")[1])
                temporary_string = (temporary_string.split("]")[0])
                temporary_list_0 = temporary_string.split(",")
                temporary_list = []
                for i in range(len(temporary_list_0)):
                    if temporary_list_0[i] != '':
                        temporary_list.append(float(temporary_list_0[i]))
                ResultFile.set_removal_usage_average_time(result_file, temporary_list)

            # removal_found_best_solution
            if "RemovalFoundBestSolution:" in line:
                temporary_string = (line.split(":")[1])
                temporary_string = (temporary_string.split("[")[1])
                temporary_string = (temporary_string.split("]")[0])
                temporary_list_0 = temporary_string.split(",")
                temporary_list = []
                for i in range(len(temporary_list_0)):
                    if temporary_list_0[i] != '':
                        temporary_list.append(int(temporary_list_0[i]))
                ResultFile.set_removal_found_best_solution(result_file, temporary_list)

            # removal_found_new_improving_solution
            if "RemovalFoundNewImprovingSolution:" in line:
                temporary_string = (line.split(":")[1])
                temporary_string = (temporary_string.split("[")[1])
                temporary_string = (temporary_string.split("]")[0])
                temporary_list_0 = temporary_string.split(",")
                temporary_list = []
                for i in range(len(temporary_list_0)):
                    if temporary_list_0[i] != '':
                        temporary_list.append(int(temporary_list_0[i]))
                ResultFile.set_removal_found_new_improving_solution(result_file, temporary_list)

            # removal_found_new_solution
            if "RemovalFoundNewSolution:" in line:
                temporary_string = (line.split(":")[1])
                temporary_string = (temporary_string.split("[")[1])
                temporary_string = (temporary_string.split("]")[0])
                temporary_list_0 = temporary_string.split(",")
                temporary_list = []
                for i in range(len(temporary_list_0)):
                    if temporary_list_0[i] != '':
                        temporary_list.append(int(temporary_list_0[i]))
                ResultFile.set_removal_found_new_solution(result_file, temporary_list)

            # removal_weights
            if "RemovalWeights:" in line:
                temporary_string = (line.split(":")[1])
                temporary_string = (temporary_string.split("[")[1])
                temporary_string = (temporary_string.split("]")[0])
                temporary_list_0 = temporary_string.split(",")
                temporary_list = []
                for i in range(len(temporary_list_0)):
                    if temporary_list_0[i] != '':
                        temporary_list.append(float(temporary_list_0[i]))
                ResultFile.set_removal_weights(result_file, temporary_list)

            # average_insertion_time
            if "AverageInsertionTime:" in line:
                ResultFile.set_average_insertion_time(result_file, float(line.split(":")[1]))

            # insertion_names
            if "InsertionNames:" in line:
                temporary_string = (line.split(":")[1])
                temporary_string = (temporary_string.split("[")[1])
                temporary_string = (temporary_string.split("]")[0])
                temporary_list = temporary_string.split(",")
                ResultFile.set_insertion_names(result_file, temporary_list)

            # insertion_usage
            if "InsertionUsage:" in line:
                temporary_string = (line.split(":")[1])
                temporary_string = (temporary_string.split("[")[1])
                temporary_string = (temporary_string.split("]")[0])
                temporary_list_0 = temporary_string.split(",")
                temporary_list = []
                for i in range(len(temporary_list_0)):
                    if temporary_list_0[i] != '':
                        temporary_list.append(int(temporary_list_0[i]))
                ResultFile.set_insertion_usage(result_file, temporary_list)

            # insertion_usage_total_time
            if "InsertionUsageTotalTime:" in line:
                temporary_string = (line.split(":")[1])
                temporary_string = (temporary_string.split("[")[1])
                temporary_string = (temporary_string.split("]")[0])
                temporary_list_0 = temporary_string.split(",")
                temporary_list = []
                for i in range(len(temporary_list_0)):
                    if temporary_list_0[i] != '':
                        temporary_list.append(float(temporary_list_0[i]))
                ResultFile.set_insertion_usage_total_time(result_file, temporary_list)

            # insertion_usage_average_time
            if "InsertionUsageAverageTime:" in line:
                temporary_string = (line.split(":")[1])
                temporary_string = (temporary_string.split("[")[1])
                temporary_string = (temporary_string.split("]")[0])
                temporary_list_0 = temporary_string.split(",")
                temporary_list = []
                for i in range(len(temporary_list_0)):
                    if temporary_list_0[i] != '':
                        temporary_list.append(float(temporary_list_0[i]))
                ResultFile.set_insertion_usage_average_time(result_file, temporary_list)

            # insertion_found_new_best_solution
            if "InsertionFoundBestSolution:" in line:
                temporary_string = (line.split(":")[1])
                temporary_string = (temporary_string.split("[")[1])
                temporary_string = (temporary_string.split("]")[0])
                temporary_list_0 = temporary_string.split(",")
                temporary_list = []
                for i in range(len(temporary_list_0)):
                    if temporary_list_0[i] != '':
                        temporary_list.append(int(temporary_list_0[i]))
                ResultFile.set_insertion_found_new_best_solution(result_file, temporary_list)

            # insertion_found_new_improving_solution
            if "InsertionFoundNewImprovingSolution:" in line:
                temporary_string = (line.split(":")[1])
                temporary_string = (temporary_string.split("[")[1])
                temporary_string = (temporary_string.split("]")[0])
                temporary_list_0 = temporary_string.split(",")
                temporary_list = []
                for i in range(len(temporary_list_0)):
                    if temporary_list_0[i] != '':
                        temporary_list.append(int(temporary_list_0[i]))
                ResultFile.set_insertion_found_new_improving_solution(result_file, temporary_list)

            # insertion_found_new_solution
            if "InsertionFoundNewSolution:" in line:
                temporary_string = (line.split(":")[1])
                temporary_string = (temporary_string.split("[")[1])
                temporary_string = (temporary_string.split("]")[0])
                temporary_list_0 = temporary_string.split(",")
                temporary_list = []
                for i in range(len(temporary_list_0)):
                    if temporary_list_0[i] != '':
                        temporary_list.append(int(temporary_list_0[i]))
                ResultFile.set_insertion_found_new_solution(result_file, temporary_list)

            # insertion_weights
            if "InsertionWeights:" in line:
                temporary_string = (line.split(":")[1])
                temporary_string = (temporary_string.split("[")[1])
                temporary_string = (temporary_string.split("]")[0])
                temporary_list_0 = temporary_string.split(",")
                temporary_list = []
                for i in range(len(temporary_list_0)):
                    if temporary_list_0[i] != '':
                        temporary_list.append(float(temporary_list_0[i]))
                ResultFile.set_insertion_weights(result_file, temporary_list)

            # # route_with_name Hvis den skal brukes må du legge inn en dictionary
            # if "InitialValue" in line:
            #     ResultFile.set_initial_value(result_file, float(line.split(":")[1]))
            #
            # # removal_weight_development Hvis den skal brukes må du legge inn en dictionary
            # if "InitialValue" in line:
            #     ResultFile.set_initial_value(result_file, float(line.split(":")[1]))
            #
            # # insertion_weight_development Hvis den skal brukes må du legge inn en dictionary
            # if "InitialValue" in line:
            #     ResultFile.set_initial_value(result_file, float(line.split(":")[1]))

        # Print for å se alle delene av filen
        # print(result_file.__dict__)

        # Print en og en del av filen
        # for key in result_file.__dict__.keys():
        #     print(key, result_file.__dict__[key])

        return result_file

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


# result_magnus = read_results_magnus()
# result_us = iterate_files()
# os.chdir("/Volumes/Seagate/MASTER/ResultsFinal/1D")
# read_results("/Volumes/Seagate/MASTER/ResultsFinal/1D/1D10R1V24-48T10-20Wr1.txt")
# start = time.time()
# iterate_files()
# end = time.time()
# print("Time on reading in all files", end-start)


start2 = time.time()
data = read_saved_data("/Volumes/Seagate/MASTER/our_results.txt")
print(data.get('1D10R1V12-24T10-20W'))
end2 = time.time()
print("Time on reading from json", end2-start2)

# print("Etter", data)
# print(data.keys())



# optimality_gaps, min_gaps, max_gaps = calculate_optimality_gap(result_magnus, result_us)
# calculate_average_gap(optimality_gaps)
# calculate_average_gap(min_gaps)
# calculate_average_gap(max_gaps)
