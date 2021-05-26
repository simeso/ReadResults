

class ResultFile:
    def __init__(self):
        pass

    def set_objective_value(self, objective_value):
        self.objective_value = objective_value

    def set_routes(self, routes):
        self.routes = routes

    def set_unhandled(self, unhandled):
        self.unhandled = unhandled

    def set_used_vehicles(self, used_vehicles):
        self.used_vehicles = used_vehicles

    def set_optimality_gap(self, optimality_gap):
        self.optimality_gap = optimality_gap

    def set_preprocessing_time(self, preprocessing_time):
        self.preprocessing_time = preprocessing_time

    def set_initial_value(self, initial_value):
        self.initial_value = initial_value

    def set_initial_solution_time(self, initial_solution_time):
        self.initial_solution_time = initial_solution_time

    def set_time_used_ALNS(self, time_used_ALNS):
        self.time_used_ALNS = time_used_ALNS

    def set_iterations_ALNS(self, iterations_ALNS):
        self.iterations_ALNS = iterations_ALNS

    def set_value_of_best_solution(self, value_of_best_solution):
        self.value_of_best_solution = value_of_best_solution

    def set_time_of_best_solution(self, time_of_best_solution):
        self.time_of_best_solution = time_of_best_solution

    def set_iterations_of_best_solution(self, iterations_of_best_solution):
        self.iterations_of_best_solution = iterations_of_best_solution

    def set_removal_operator_of_best_solution(self, removal_operator_of_best_solution):
        self.removal_operator_of_best_solution = removal_operator_of_best_solution

    def set_insertion_operator_of_best_solution(self, insertion_operator_of_best_solution):
        self.insertion_operator_of_best_solution = insertion_operator_of_best_solution

    def set_scheduling_insertion_did_nothing(self, scheduling_insertion_did_nothing):
        self.scheduling_insertion_did_nothing = scheduling_insertion_did_nothing

    def set_num_calls_scheduling(self, num_calls_scheduling):
        self.num_calls_scheduling = num_calls_scheduling

    def set_average_time_scheduling(self, average_time_scheduling):
        self.average_time_scheduling = average_time_scheduling

    def set_num_feasibility_checks(self, num_feasibility_checks):
        self.num_feasibility_checks = num_feasibility_checks

    def set_num_previously_checked(self, num_previously_checked):
        self.num_previously_checked = num_previously_checked

    def set_percentage_previously_checked(self, percentage_previously_checked):
        self.percentage_previously_checked = percentage_previously_checked

    def set_average_removal_time(self, average_removal_time):
        self.average_removal_time = average_removal_time

    def set_removal_not_used(self, removal_not_used):
        self.removal_not_used = removal_not_used

    def set_removal_names(self, removal_names):
        self.removal_names = removal_names

    def set_removal_usage(self, removal_usage):
        self.removal_usage = removal_usage

    def set_removal_usage_total_time(self, removal_usage_total_time):
        self.removal_usage_total_time = removal_usage_total_time

    def set_removal_usage_average_time(self, removal_usage_average_time):
        self.removal_usage_average_time = removal_usage_average_time

    def set_removal_found_best_solution(self, removal_found_best_solution):
        self.removal_found_best_solution = removal_found_best_solution

    def set_removal_found_new_improving_solution(self, removal_found_new_improving_solution):
        self.removal_found_new_improving_solution = removal_found_new_improving_solution

    def set_removal_found_new_solution(self, removal_found_new_solution):
        self.removal_found_new_solution = removal_found_new_solution

    def set_removal_weights(self, removal_weights):
        self.removal_weights = removal_weights

    def set_average_insertion_time(self, average_insertion_time):
        self.average_insertion_time = average_insertion_time

    def set_insertion_names(self, insertion_names):
        self.insertion_names = insertion_names

    def set_insertion_usage(self, insertion_usage):
        self.insertion_usage = insertion_usage

    def set_insertion_usage_total_time(self, insertion_usage_total_time):
        self.insertion_usage_total_time = insertion_usage_total_time

    def set_insertion_usage_average_time(self, insertion_usage_average_time):
        self.insertion_usage_average_time = insertion_usage_average_time

    def set_insertion_found_new_best_solution(self, insertion_found_new_best_solution):
        self.insertion_found_new_best_solution = insertion_found_new_best_solution

    def set_insertion_found_new_improving_solution(self, insertion_found_new_improving_solution):
        self.insertion_found_new_improving_solution = insertion_found_new_improving_solution

    def set_insertion_found_new_solution(self, insertion_found_new_solution):
        self.insertion_found_new_solution = insertion_found_new_solution

    def set_insertion_weights(self, insertion_weights):
        self.insertion_weights = insertion_weights

    # def set_route_with_name(self, route_with_name):
    #     self.route_with_name = route_with_name
    #
    # def set_removal_weight_development(self, removal_weight_development):
    #     self.removal_weight_development = removal_weight_development
    #
    # def set_insertion_weight_development(self, insertion_weight_development):
    #     self.insertion_weight_development = insertion_weight_development
